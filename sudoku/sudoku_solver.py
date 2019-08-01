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


def check_column_for_value(sudoku, column: int, value: int) -> bool:
    return value in sudoku.board[:, column]


def get_rows_from_box_index(box_numer: int) -> List[int]:
    if 0 <= box_numer < 3:
        rows = [0, 1, 2]
    elif 3 <= box_numer < 6:
        rows = [3, 4, 5]
    elif 6 <= box_numer < 9:
        rows = [6, 7, 8]

    return rows


def get_columns_from_box_index(box_numer: int) -> List[int]:
    if box_numer % 3 == 0:
        columns = [0, 1, 2]
    elif box_numer % 3 == 1:
        columns = [3, 4, 5]
    elif box_numer % 3 == 2:
        columns = [6, 7, 8]

    return columns


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
        possible_rows = []
        possible_columns = []

        # for each row in the box
        for row in get_rows_from_box_index(box_number):
            # If the value is not in that row then it could be in that row
            # of the box.
            if not check_row_for_value(sudoku, row, value):
                possible_rows.append(row)
        # for each column in the box
        for column in get_columns_from_box_index(box_number):
            # If the value is not in that column then it could be in that column
            # of the box.
            if not check_column_for_value(sudoku, column, value):
                possible_columns.append(column)

        # If there is a single value for possible rows and columns,
        # then add that value to this index.
        possible_rows = list(set(possible_rows))
        possible_columns = list(set(possible_columns))

        if len(possible_columns) == 1:
            for row in possible_rows:
                if sudoku.board[row, possible_columns[0]] != 0:
                    possible_rows.remove(row)

        if len(possible_rows) == 1:
            for column in possible_columns:
                if sudoku.board[possible_rows[0], column] != 0:
                    possible_columns.remove(column)

        if len(possible_columns) == 1 and len(possible_rows) == 1:
            sudoku.board[possible_rows[0], possible_columns[0]] = value


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
