from Soduku import Soduku
from numpy import array

valid_board = [[2, 4, 8, 3, 9, 5, 7, 1, 6],
               [5, 7, 1, 6, 2, 8, 3, 4, 9],
               [9, 3, 6, 7, 4, 1, 5, 8, 2],
               [6, 8, 2, 5, 3, 9, 1, 7, 4],
               [3, 5, 9, 1, 7, 4, 6, 2, 8],
               [7, 1, 4, 8, 6, 2, 9, 5, 3],
               [8, 6, 3, 4, 1, 7, 2, 9, 5],
               [1, 9, 5, 2, 8, 6, 4, 3, 7],
               [4, 2, 7, 9, 5, 3, 8, 6, 1]]

invalid_board = [[1, 1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1]]


def test_init_with_valid_board():
    soduku = Soduku(valid_board)
    board_out = soduku.get_board()
    assert (array(valid_board) == board_out).all()


def test_verify_row_with_valid_rows():
    soduku = Soduku(valid_board)
    for i in range(9):
        assert soduku.verify_row(i)


def test_verify_row_with_invalid_rows():
    soduku = Soduku(invalid_board)
    for i in range(9):
        assert not soduku.verify_row(i)


def test_verify_column_with_valid_columns():
    soduku = Soduku(valid_board)
    for i in range(9):
        assert soduku.verify_column(i)


def test_verify_column_with_invalid_columns():
    soduku = Soduku(invalid_board)
    for i in range(9):
        assert not soduku.verify_column(i)


def test_verify_box_with_valid_boxes():
    soduku = Soduku(valid_board)
    for i in range(9):
        assert soduku.verify_box(i)


def test_verify_box_with_invalid_boxes():
    soduku = Soduku(invalid_board)
    for i in range(9):
        assert not soduku.verify_box(i)


def test_verify_board_with_valid():
    soduku = Soduku(valid_board)
    assert soduku.verify_board()


def test_verify_board_with_invalid():
    soduku = Soduku(invalid_board)
    assert not soduku.verify_board()
