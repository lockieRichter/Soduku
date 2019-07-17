import pytest
import boards
from sudoku_board import Sudoku
from numpy import array


def test_init_with_valid_board():
    sudoku_board = Sudoku(boards.valid)
    board_out = sudoku_board.board
    assert (array(boards.valid) == board_out).all()


def test_add_cell_with_valid():
    sudoku_board = Sudoku(boards.initial)
    row = 3
    column = 7
    value = 5
    sudoku_board.add_cell(row, column, value)
    assert sudoku_board.board[row][column] == value


def test_add_cell_with_invalid():
    sudoku_board = Sudoku(boards.initial)
    row = 3
    column = 7
    value = 's'
    with pytest.raises(Exception):
        sudoku_board.add_cell(row, column, value)


def test_get_box_with_valid():
    sudoku_board = Sudoku(boards.initial)

    box1 = sudoku_board.get_box(0, 0)
    expected_box1 = array([[5, 3, 0], [6, 0, 0], [0, 9, 8]])
    assert box1.all() == expected_box1.all()

    box2 = sudoku_board.get_box(1, 3)
    expected_box2 = array([[0, 7, 0], [1, 9, 5], [0, 0, 0]])
    assert box2.all() == expected_box2.all()

    box6 = sudoku_board.get_box(3, 8)
    expected_box6 = array([[0, 7, 0], [1, 9, 5], [0, 0, 0]])
    assert box6.all() == expected_box6.all()

    box7 = sudoku_board.get_box(8, 2)
    expected_box7 = array([[0, 7, 0], [1, 9, 5], [0, 0, 0]])
    assert box7.all() == expected_box7.all()

    box9 = sudoku_board.get_box(6, 6)
    expected_box9 = array([[0, 7, 0], [1, 9, 5], [0, 0, 0]])
    assert box9.all() == expected_box9.all()
