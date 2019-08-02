from itertools import chain
from typing import List
from typing import Tuple

from numpy import unique


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


def check_column_for_value(sudoku, column: int, value: int) -> bool:
    return value in sudoku.board[:, column]


def get_rows_from_box_index(box_number: int) -> List[int]:
    rows = []
    if 0 <= box_number < 3:
        rows = [0, 1, 2]
    elif 3 <= box_number < 6:
        rows = [3, 4, 5]
    elif 6 <= box_number < 9:
        rows = [6, 7, 8]

    return rows


def get_columns_from_box_index(box_number: int) -> List[int]:
    columns = []
    if box_number % 3 == 0:
        columns = [0, 1, 2]
    elif box_number % 3 == 1:
        columns = [3, 4, 5]
    elif box_number % 3 == 2:
        columns = [6, 7, 8]

    return columns


def crosshatch_box(sudoku, box_number: int) -> bool:
    all_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    unused_values = []

    box = sudoku.get_box_from_index(box_number)
    box_values = box.flatten()

    for value in all_values:
        if value not in box_values:
            unused_values.append(value)

    solved_value = False
    # Loop through each value that is not in the box.
    for value in unused_values:
        possible_rows = []
        possible_columns = []

        # Check each row that goes through the box.
        for row in get_rows_from_box_index(box_number):
            # If the value is not in that row then it could be in that row of the box.
            if not check_row_for_value(sudoku, row, value):
                possible_rows.append(row)
        # Check each column that goes through the box.
        for column in get_columns_from_box_index(box_number):
            # If the value is not in that column then it could be in that column of the box.
            if not check_column_for_value(sudoku, column, value):
                possible_columns.append(column)

        # Remove duplicates from possible rows and columns.
        possible_rows = list(set(possible_rows))
        possible_columns = list(set(possible_columns))

        # A cell position is only possible if the value is 0. Save the index if it is.
        possible_index = []
        for row in possible_rows:
            for column in possible_columns:
                if sudoku.board[row, column] == 0:
                    possible_index.append([row, column])

        # If there is only one possible value for this cell then add it to the board.
        if len(possible_index) == 1:
            sudoku.board[possible_index[0][0], possible_index[0][1]] = value
            solved_value = True

    return solved_value


def solve_all_crosshatch_boxes(sudoku) -> None:
    solved_value = True
    while solved_value:
        solved_value = False
        for box_number in range(9):
            solved_value = crosshatch_box(sudoku, box_number)


def get_adjacent_rows_and_columns(row: int, column: int) -> Tuple[List[int], List[int]]:
    first = [0, 1, 2]
    second = [3, 4, 5]
    third = [6, 7, 8]

    rows = []
    columns = []
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
