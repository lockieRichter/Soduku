from sudoku import sudoku_solver, boards, sudoku_gui


def test_gui_fast():
    gui = sudoku_gui.Gui()
    gui.solve_fast = True
    gui.add_value_to_gui(0, 0, 1)
    gui.solve_clicked()
    gui.close_window()
    assert sudoku_solver.verify_board(gui.sudoku)
    assert (gui.sudoku.board_numbers == boards.empty_solved).all()


def test_gui_slow():
    gui = sudoku_gui.Gui()
    gui.add_value_to_gui(0, 0, 1)
    gui.solve_clicked()
    gui.close_window()
    assert sudoku_solver.verify_board(gui.sudoku)
    assert (gui.sudoku.board_numbers == boards.empty_solved).all()
