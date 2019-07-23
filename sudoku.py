import fileinput
from sudoku import sudoku_solver, boards

from sudoku.sudoku_board import Sudoku


def read_board_in():
    board_in = [[0] * 9 for i in range(9)]
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
print("Please enter the Soduku board in rows of 9, separating numbers with a space.")
print("Enter 0 for any number that is unknown.")

board = read_board_in()

sudoku = Sudoku(board)

print("You entered the following board...")
sudoku.print_board()
print("Is that correct? (yes/no)")

correct = input()
if correct.strip() != "yes":
    board = read_board_in()

sudoku_solver.solve_all_single_value_cells(sudoku)

if sudoku_solver.verify_board(sudoku):
    print("Have completed the board with the following solution...")
else:
    print("Could not solve board using single values.")
    print("Have solved the board to the following values...")

sudoku.print_board()

