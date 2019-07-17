from numpy import unique
from itertools import chain


def verify_row(sudoku, row):
    row_values = sudoku.board[row][:]
    if len(row_values) > len(set(row_values)):
        return False
    else:
        return True


def verify_column(sudoku, column):
    column_values = sudoku.board[:][column]
    if len(column_values) > len(set(column_values)):
        return False
    else:
        return True


def verify_box(sudoku, box):
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

    if len(unique(box_values)) != 9:
        return False
    else:
        return True


def verify_board(sudoku):
    for i in range(9):
        if not (verify_row(sudoku, i) and verify_column(sudoku, i) and verify_box(sudoku, i)):
            return False
        else:
            return True


def non_zero(value):
    if value != 0:
        return True
    else:
        return False


def get_possible_values(sudoku, row, column):
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




