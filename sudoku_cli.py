import fileinput

from sudoku import sudoku_solver, boards
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


print("Welcome to Soduku solver...")

correct = "no"
while correct.strip() != "yes":
    print("Please enter the Soduku board in rows of 9, separating numbers with a space.")
    print("Enter 0 for any number that is unknown.")
    board = read_board_in()
    sudoku = Sudoku(board)

    print("You entered the following board...")
    sudoku.print_board()
    print("Is that correct? (yes/no)")
    correct = input()

iterations = 0
while not sudoku_solver.verify_board(sudoku):
    iterations += 1
    sudoku_solver.solve_all_single_value_cells(sudoku)
    sudoku_solver.solve_all_crosshatch_boxes(sudoku)
    sudoku_solver.solve_all_naked_subsets(sudoku)

    if iterations == 20:
        print("Could not find a solution after 20 iterations.")
        print("Have solved the board to the following point...")
        sudoku.print_board()
        print("Will now try to brute force solve the board...")
        sudoku_solver.solve_sudoku(sudoku.board_numbers)

if sudoku_solver.verify_board(sudoku):
    print("Have completed the board with the following solution, after {0} iterations...".format(iterations))
    sudoku.print_board()
