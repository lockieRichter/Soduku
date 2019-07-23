from numpy import unique
from itertools import chain


def verify_row(sudoku, row):
    row_values = sudoku.board[row][:]
    return len(row_values) <= len(set(row_values))


def verify_column(sudoku, column):
    column_values = sudoku.board[:][column]
    return len(column_values) <= len(set(column_values))


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

    return len(unique(box_values)) == 9


def verify_board(sudoku):
    for i in range(9):
        if not (verify_row(sudoku, i) and verify_column(sudoku, i) and verify_box(sudoku, i)):
            return False
    return True


def non_zero(value):
    return value != 0


def get_possible_cell_values(sudoku, row, column):
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


def solve_all_single_value_cells(sudoku):
    solved_value = True
    while solved_value:
        solved_value = False
        for row in range(9):
            for column in range(9):
                values = get_possible_cell_values(sudoku, row, column)
                if len(values) == 1 and sudoku.board[row][column] == 0:
                    sudoku.add_cell(row, column, values[0])
                    solved_value = True
