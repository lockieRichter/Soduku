import boards
import sudoku_solver
from sudoku_board import Sudoku


def test_verify_row_with_valid_rows():
    sudoku_board = Sudoku(boards.valid)
    for i in range(9):
        assert sudoku_solver.verify_row(sudoku_board, i)


def test_verify_row_with_invalid_rows():
    sudoku_board = Sudoku(boards.invalid)
    for i in range(9):
        assert not sudoku_solver.verify_row(sudoku_board, i)


def test_verify_row_with_valid_rows():
    sudoku_board = Sudoku(boards.valid)
    for i in range(9):
        assert sudoku_solver.verify_row(sudoku_board, i)


def test_verify_row_with_invalid_rows():
    sudoku_board = Sudoku(boards.invalid)
    for i in range(9):
        assert not sudoku_solver.verify_row(sudoku_board, i)


def test_verify_column_with_valid_columns():
    sudoku_board = Sudoku(boards.valid)
    for i in range(9):
        assert sudoku_solver.verify_column(sudoku_board, i)


def test_verify_column_with_invalid_columns():
    sudoku_board = Sudoku(boards.invalid)
    for i in range(9):
        assert not sudoku_solver.verify_column(sudoku_board, i)


def test_verify_box_with_valid_boxes():
    sudoku_board = Sudoku(boards.valid)
    for i in range(9):
        assert sudoku_solver.verify_box(sudoku_board, i)


def test_verify_box_with_invalid_boxes():
    sudoku_board = Sudoku(boards.invalid)
    for i in range(9):
        assert not sudoku_solver.verify_box(sudoku_board, i)


def test_verify_board_with_valid():
    sudoku_board = Sudoku(boards.valid)
    assert sudoku_solver.verify_board(sudoku_board)


def test_verify_board_with_invalid():
    sudoku_board = Sudoku(boards.invalid)
    assert not sudoku_solver.verify_board(sudoku_board)


def test_non_zero_with_zero():
    zero = 0
    assert not sudoku_solver.non_zero(zero)


def test_non_zero_with_non_zero():
    not_zero = 9
    assert sudoku_solver.non_zero(not_zero)


def test_get_possible_values_with_initial():
    sudoku_board = Sudoku(boards.initial)

    possible_values = sudoku_solver.get_possible_values(sudoku_board, 0, 2)
    assert possible_values == [1, 2, 4]

    possible_values = sudoku_solver.get_possible_values(sudoku_board, 0, 1)
    assert possible_values == [3]

    possible_values = sudoku_solver.get_possible_values(sudoku_board, 8, 8)
    assert possible_values == [9]
