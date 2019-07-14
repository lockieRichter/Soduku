import pytest
import boards
from soduku_board import Soduku
from numpy import array


def test_init_with_valid_board():
    soduku_board = Soduku(boards.valid)
    board_out = soduku_board.board
    assert (array(boards.valid) == board_out).all()


def test_add_cell_with_valid():
    soduku_board = Soduku(boards.initial)
    row = 3
    column = 7
    value = 5
    soduku_board.add_cell(row, column, value)
    assert soduku_board.board[row][column] == value


def test_add_cell_with_invalid():
    soduku_board = Soduku(boards.initial)
    row = 3
    column = 7
    value = 's'
    with pytest.raises(Exception):
        soduku_board.add_cell(row, column, value)
