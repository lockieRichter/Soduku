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


def test_get_box_with_valid():
    soduku_board = Soduku(boards.initial)

    box1 = soduku_board.get_box(0, 0)
    expected_box1 = array([[5, 3, 0], [6, 0, 0], [0, 9, 8]])
    assert box1.all() == expected_box1.all()

    box2 = soduku_board.get_box(1, 3)
    expected_box2 = array([[0, 7, 0], [1, 9, 5], [0, 0, 0]])
    assert box2.all() == expected_box2.all()

    box6 = soduku_board.get_box(3, 8)
    expected_box6 = array([[0, 7, 0], [1, 9, 5], [0, 0, 0]])
    assert box6.all() == expected_box6.all()

    box7 = soduku_board.get_box(8, 2)
    expected_box7 = array([[0, 7, 0], [1, 9, 5], [0, 0, 0]])
    assert box7.all() == expected_box7.all()

    box9 = soduku_board.get_box(6, 6)
    expected_box9 = array([[0, 7, 0], [1, 9, 5], [0, 0, 0]])
    assert box9.all() == expected_box9.all()
