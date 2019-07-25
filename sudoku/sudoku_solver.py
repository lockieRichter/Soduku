from numpy import unique
from itertools import chain
from typing import List


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
        box_values = sudoku.get_box(row, column).flatten()

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


# TODO: Need to finish implementing solver for unique cadidates.
def solve_all_unique_value_cells(sudoku) -> None:
    for row in range(9):
        for column in range(9):
            if sudoku.board[row, column] == 0:
                possible_values = get_possible_cell_values(sudoku, row, column)


# TODO: Need to finish implementing solver for unique cadidates.
def check_for_unique_candidate(sudoku, row: int, column: int):
    first = [0, 1, 2]
    second = [3, 4, 5]
    third = [6, 7, 8]

    if row // 3 == 0:
        rows = first
    elif row // 3 == 1:
        rows = second
    elif row // 3 == 2:
        rows = third

    rows.remove(row)

    if column // 3 == 0:
        columns = first
    elif column // 3 == 1:
        columns = second
    elif column // 3 == 2:
        columns = third

    columns.remove(column)
