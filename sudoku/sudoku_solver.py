from numpy import unique
from numpy import delete
from itertools import chain
from typing import List
from typing import Tuple


def verify_row(sudoku, row: int) -> bool:
    row_values = sudoku.board[row][:]
    return len(row_values) <= len(set(row_values))


def verify_column(sudoku, column: int) -> bool:
    column_values = sudoku.board[:][column]
    return len(column_values) <= len(set(column_values))


def verify_box(sudoku, box: int) -> bool:
    d = box // 3
    r = box % 3
    box_values = None

    if d == 0:
        box_values = sudoku.board[:, :3]
    elif d == 1:
        box_values = sudoku.board[:, 3:6]
    elif d == 2:
        box_values = sudoku.board[:, 6:]

    if r == 0:
        box_values = box_values[:3, :]
    elif r == 1:
        box_values = box_values[3:6, :]
    elif r == 2:
        box_values = box_values[6:, :]

    return len(unique(box_values)) == 9


def verify_board(sudoku) -> bool:
    for i in range(9):
        if not (verify_row(sudoku, i) and verify_column(sudoku, i) and verify_box(sudoku, i)):
            return False
    return True


def non_zero(value: int) -> bool:
    return value != 0


def get_possible_cell_values(sudoku, row: int, column: int) -> List[int]:
    all_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    possible_values = []

    if sudoku.board[row][column] != 0:
        possible_values.append(sudoku.board[row][column])
    else:
        row_values = sudoku.board[row, :].flatten()
        column_values = sudoku.board[:, column].flatten()
        box_values = sudoku.get_box_from_cell(row, column).flatten()

        used_values = unique(list(filter(non_zero, chain(row_values, column_values, box_values))))

        for value in all_values:
            if value not in used_values:
                possible_values.append(value)

    return possible_values


def solve_all_single_value_cells(sudoku) -> None:
    solved_value = True
    while solved_value:
        solved_value = False
        for row in range(9):
            for column in range(9):
                values = get_possible_cell_values(sudoku, row, column)
                if len(values) == 1 and sudoku.board[row][column] == 0:
                    sudoku.add_cell(row, column, values[0])
                    solved_value = True


def check_row_for_value(sudoku, row: int, value: int) -> bool:
    return value in sudoku.board[row, :]


def crosshatch_box(sudoku, box_number: int) -> None:
    all_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    unused_values = []

    box = sudoku.get_box_from_index(box_number)
    box_values = box.flatten()

    for value in all_values:
        if value not in box_values:
            unused_values.append(value)

    # for each value that is not in the box
    for value in unused_values:
        # TODO: Update row to be correct for box.
        row = 1
        check_row_for_value(sudoku, row, value)

# check each row for that value
# if that value is in the row, then it can't be in that row of the box
# else add the row to possible rows.
# check each column for that value
# if that value is in the column, then it caN't be in the column of the box
# else add the column to possible columns.
# if there is a single value for possible rows and columns, then add that value to this index


def get_adjacent_rows_and_columns(row: int, column: int) -> Tuple[List[int], List[int]]:
    first = [0, 1, 2]
    second = [3, 4, 5]
    third = [6, 7, 8]

    if row // 3 == 0:
        rows = first.copy()
    elif row // 3 == 1:
        rows = second.copy()
    elif row // 3 == 2:
        rows = third.copy()

    rows.remove(row)

    if column // 3 == 0:
        columns = first.copy()
    elif column // 3 == 1:
        columns = second.copy()
    elif column // 3 == 2:
        columns = third.copy()

    columns.remove(column)

    return rows, columns

# TODO: Do we need this at all?
# def check_for_adjacent_values(sudoku, row: int, column: int):
#     if row % 3 == 0:
#         row_values = sudoku.board[row + 1, :].copy()
#     elif row % 3 == 1:
#         row_values = delete(sudoku.board[row - 1: row + 2, :].copy(), 1, 0)
#     elif row % 3 == 2:
#         row_values = sudoku.board[row - 1, :].copy()
#
#     if column % 3 == 0:
#         column_values = sudoku.board[:, column + 1].copy()
#     elif column % 3 == 1:
#         column_values = delete(sudoku.board[:, column - 1: column + 2].copy(), 1, 0)
#     elif column % 3 == 2:
#         column_values = sudoku.board[:, column - 1].copy()
#
#     value = sudoku.board[row, column]

# TODO: Need to finish implementing solver for unique cadidates.
# def check_for_unique_candidate(sudoku, row: int, column: int) -> int:
#     adjacent_rows, adjacent_columns = get_adjacent_rows_and_columns(row, column)

# TODO: Need to finish implementing solver for unique cadidates.
# def solve_all_unique_value_cells(sudoku) -> None:
#     for row in range(9):
#         for column in range(9):
#             if sudoku.board[row, column] == 0:
#                 possible_values = get_possible_cell_values(sudoku, row, column)
