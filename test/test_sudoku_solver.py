from numpy import array

from sudoku import sudoku_solver, boards
from sudoku.sudoku_board import Sudoku


def test_verify_row_with_valid_rows():
    sudoku_board = Sudoku(boards.solved)
    for i in range(9):
        assert sudoku_solver.verify_row(sudoku_board, i)


def test_verify_row_with_invalid_rows():
    sudoku_board = Sudoku(boards.invalid)
    for i in range(9):
        assert not sudoku_solver.verify_row(sudoku_board, i)


def test_verify_column_with_valid_columns():
    sudoku_board = Sudoku(boards.solved)
    for i in range(9):
        assert sudoku_solver.verify_column(sudoku_board, i)


def test_verify_column_with_invalid_columns():
    sudoku_board = Sudoku(boards.invalid)
    for i in range(9):
        assert not sudoku_solver.verify_column(sudoku_board, i)


def test_verify_box_with_valid_boxes():
    sudoku_board = Sudoku(boards.solved)
    for i in range(9):
        assert sudoku_solver.verify_box(sudoku_board, i)


def test_verify_box_with_invalid_boxes():
    sudoku_board = Sudoku(boards.invalid)
    for i in range(9):
        assert not sudoku_solver.verify_box(sudoku_board, i)


def test_verify_board_with_valid():
    sudoku_board = Sudoku(boards.solved)
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


def test_get_possible_cell_values_with_unsolved_easy():
    sudoku_board = Sudoku(boards.unsolved_easy)

    possible_values = sudoku_solver.get_possible_cell_values(sudoku_board, 0, 2)
    assert possible_values == [1, 2, 4]

    possible_values = sudoku_solver.get_possible_cell_values(sudoku_board, 0, 1)
    assert possible_values == [3]

    possible_values = sudoku_solver.get_possible_cell_values(sudoku_board, 8, 8)
    assert possible_values == [9]


def test_solve_all_single_value_cells_with_unsolved_easy():
    sudoku_board = Sudoku(boards.unsolved_easy)
    sudoku_solver.solve_all_single_value_cells(sudoku_board)
    solved_board = sudoku_board.board
    expected_board = boards.solved_easy
    assert (array(expected_board) == solved_board).all()


def test_get_adjacent_rows_and_columns():
    rows, columns = sudoku_solver.get_adjacent_rows_and_columns(0, 0)
    assert rows == [1, 2]
    assert columns == [1, 2]

    rows, columns = sudoku_solver.get_adjacent_rows_and_columns(3, 5)
    assert rows == [4, 5]
    assert columns == [3, 4]

    rows, columns = sudoku_solver.get_adjacent_rows_and_columns(7, 8)
    assert rows == [6, 8]
    assert columns == [6, 7]


def test_check_row_for_value():
    sudoku = Sudoku(boards.unique_candidate_test)
    assert sudoku_solver.check_row_for_value(sudoku, 0, 4)
    assert not sudoku_solver.check_row_for_value(sudoku, 0, 5)


def test_check_column_for_value():
    sudoku = Sudoku(boards.unique_candidate_test)
    assert sudoku_solver.check_column_for_value(sudoku, 2, 4)
    assert not sudoku_solver.check_column_for_value(sudoku, 2, 5)


def test_get_rows_from_box_index():
    rows = sudoku_solver.get_rows_from_box_index(0)
    expected_rows = [0, 1, 2]
    assert rows == expected_rows

    rows = sudoku_solver.get_rows_from_box_index(4)
    expected_rows = [3, 4, 5]
    assert rows == expected_rows

    rows = sudoku_solver.get_rows_from_box_index(8)
    expected_rows = [6, 7, 8]
    assert rows == expected_rows


def test_get_columns_from_box_index():
    columns = sudoku_solver.get_columns_from_box_index(0)
    expected_columns = [0, 1, 2]
    assert columns == expected_columns

    columns = sudoku_solver.get_columns_from_box_index(4)
    expected_columns = [3, 4, 5]
    assert columns == expected_columns

    columns = sudoku_solver.get_columns_from_box_index(8)
    expected_columns = [6, 7, 8]
    assert columns == expected_columns


def test_crosshatch_box():
    sudoku_board = Sudoku(boards.unique_candidate_test)
    assert sudoku_board.board[7, 0] == 0
    sudoku_solver.crosshatch_box(sudoku_board, 6)
    assert sudoku_board.board[7, 0] == 4

    sudoku_board = Sudoku(boards.unsolved_hard)
    assert sudoku_board.board[5, 6] == 0
    sudoku_solver.crosshatch_box(sudoku_board, 5)
    assert sudoku_board.board[5, 6] == 8


def test_solve_all_crosshatch_boxes():
    sudoku_board = Sudoku(boards.unique_candidate_test)
    assert sudoku_board.board[7, 0] == 0
    sudoku_solver.solve_all_crosshatch_boxes(sudoku_board)
    assert sudoku_board.board[7, 0] == 4
