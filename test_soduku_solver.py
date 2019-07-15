import boards
import soduku_solver
from soduku_board import Soduku


def test_verify_row_with_valid_rows():
    soduku_board = Soduku(boards.valid)
    for i in range(9):
        assert soduku_solver.verify_row(soduku_board, i)


def test_verify_row_with_invalid_rows():
    soduku_board = Soduku(boards.invalid)
    for i in range(9):
        assert not soduku_solver.verify_row(soduku_board, i)


def test_verify_row_with_valid_rows():
    soduku_board = Soduku(boards.valid)
    for i in range(9):
        assert soduku_solver.verify_row(soduku_board, i)


def test_verify_row_with_invalid_rows():
    soduku_board = Soduku(boards.invalid)
    for i in range(9):
        assert not soduku_solver.verify_row(soduku_board, i)


def test_verify_column_with_valid_columns():
    soduku_board = Soduku(boards.valid)
    for i in range(9):
        assert soduku_solver.verify_column(soduku_board, i)


def test_verify_column_with_invalid_columns():
    soduku_board = Soduku(boards.invalid)
    for i in range(9):
        assert not soduku_solver.verify_column(soduku_board, i)


def test_verify_box_with_valid_boxes():
    soduku_board = Soduku(boards.valid)
    for i in range(9):
        assert soduku_solver.verify_box(soduku_board, i)


def test_verify_box_with_invalid_boxes():
    soduku_board = Soduku(boards.invalid)
    for i in range(9):
        assert not soduku_solver.verify_box(soduku_board, i)


def test_verify_board_with_valid():
    soduku_board = Soduku(boards.valid)
    assert soduku_solver.verify_board(soduku_board)


def test_verify_board_with_invalid():
    soduku_board = Soduku(boards.invalid)
    assert not soduku_solver.verify_board(soduku_board)


def test_non_zero_with_zero():
    zero = 0
    assert not soduku_solver.non_zero(zero)


def test_non_zero_with_non_zero():
    not_zero = 9
    assert soduku_solver.non_zero(not_zero)
