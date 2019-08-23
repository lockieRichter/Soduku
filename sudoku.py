import fileinput
from argparse import ArgumentParser

from sudoku import sudoku_solver, boards, sudoku_gui
from sudoku.sudoku_board import Sudoku


def read_board_in():
    board_in = boards.empty
    count = 0
    for line in fileinput.input():
        board_in[count] = line.split()
        count = count + 1
        if count == 9:
            break

    for i in range(9):
        for j in range(9):
            board_in[i][j] = int(board_in[i][j])

    return board_in


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("-g", "--gui", dest="use_gui",
                        help="Use the GUI.", default=False, action="store_true")

    args = parser.parse_args()
    if args.use_gui:
        gui = sudoku_gui.Gui()
        gui.window.mainloop()
    else:
        print("Welcome to Soduku solver...")
        correct = "no"
        sudoku = None
        while correct.strip() != "yes":
            print("Please enter the Soduku board in rows of 9, separating numbers with a space.")
            print("Enter 0 for any number that is unknown.")
            board = read_board_in()
            sudoku = Sudoku(board)

            print("You entered the following board...")
            sudoku.print_board()
            print("Is that correct? (yes/no)")
            correct = input()
        sudoku_solver.solve_board(sudoku)
