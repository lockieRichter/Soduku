import pytest
from sudoku import boards
from sudoku.sudoku_board import Sudoku
from numpy import array


def test_init_with_valid_board():
    sudoku_board = Sudoku(boards.solved)
    board_out = sudoku_board.board
    assert (array(boards.solved) == board_out).all()


def test_add_cell_with_valid():
    sudoku_board = Sudoku(boards.unsolved_easy)
    row = 3
    column = 7
    value = 5
    sudoku_board.add_cell(row, column, value)
    assert sudoku_board.board[row][column] == value


def test_add_cell_with_invalid():
    sudoku_board = Sudoku(boards.unsolved_easy)
    row = 3
    column = 7
    value = 's'
    with pytest.raises(Exception):
        sudoku_board.add_cell(row, column, value)


def test_get_box_from_cell_with_valid():
    sudoku_board = Sudoku(boards.unsolved_easy)

    box1 = sudoku_board.get_box_from_cell(0, 0)
    expected_box1 = array([[5, 3, 0], [6, 0, 0], [0, 9, 8]])
    assert (box1 == expected_box1).all()

    box2 = sudoku_board.get_box_from_cell(1, 3)
    expected_box2 = array([[0, 7, 0], [1, 9, 5], [0, 0, 0]])
    assert (box2 == expected_box2).all()

    box6 = sudoku_board.get_box_from_cell(3, 8)
    expected_box6 = array([[0, 0, 3], [0, 0, 1], [0, 0, 6]])
    assert (box6 == expected_box6).all()

    box7 = sudoku_board.get_box_from_cell(8, 2)
    expected_box7 = array([[0, 6, 0], [0, 0, 0], [0, 0, 0]])
    assert (box7 == expected_box7).all()

    box9 = sudoku_board.get_box_from_cell(6, 6)
    expected_box9 = array([[2, 8, 0], [0, 0, 5], [0, 7, 9]])
    assert (box9 == expected_box9).all()


def test_get_box_from_index():
    sudoku_board = Sudoku(boards.unsolved_easy)

    box1 = sudoku_board.get_box_from_index(0)
    expected_box1 = array([[5, 3, 0], [6, 0, 0], [0, 9, 8]])
    assert (box1 == expected_box1).all()

    box2 = sudoku_board.get_box_from_index(1)
    expected_box2 = array([[0, 7, 0], [1, 9, 5], [0, 0, 0]])
    assert (box2 == expected_box2).all()

    box3 = sudoku_board.get_box_from_index(2)
    expected_box3 = array([[0, 0, 0], [0, 0, 0], [0, 6, 0]])
    assert (box3 == expected_box3).all()

    box4 = sudoku_board.get_box_from_index(3)
    expected_box4 = array([[8, 0, 0], [4, 0, 0], [7, 0, 0]])
    assert (box4 == expected_box4).all()

    box5 = sudoku_board.get_box_from_index(4)
    expected_box5 = array([[0, 6, 0], [8, 0, 3], [0, 2, 0]])
    assert (box5 == expected_box5).all()

    box6 = sudoku_board.get_box_from_index(5)
    expected_box6 = array([[0, 0, 3], [0, 0, 1], [0, 0, 6]])
    assert (box6 == expected_box6).all()

    box7 = sudoku_board.get_box_from_index(6)
    expected_box7 = array([[0, 6, 0], [0, 0, 0], [0, 0, 0]])
    assert (box7 == expected_box7).all()

    box8 = sudoku_board.get_box_from_index(7)
    expected_box8 = array([[0, 0, 0], [4, 1, 9], [0, 8, 0]])
    assert (box8 == expected_box8).all()

    box9 = sudoku_board.get_box_from_index(8)
    expected_box9 = array([[2, 8, 0], [0, 0, 5], [0, 7, 9]])
    assert (box9 == expected_box9).all()


def test_print_board(capsys):
    sudoku_board = Sudoku(boards.unsolved_easy)
    sudoku_board.print_board()
    expected = boards.printed_board
    out, err = capsys.readouterr()
    assert out == expected
