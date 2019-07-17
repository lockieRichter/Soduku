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
    return board_in


print("Welcome to Soduku solver...")
print("Please enter the Soduku board in rows of 9, separating numbers with a space.")
print("Enter 0 for any number that is unknown.")

# board = read_board_in()

sudoku = Sudoku(boards.initial)

print("You entered the following board..")
sudoku.print_board()
print("Is that correct? (yes/no)")

possible_values = sudoku_solver.get_possible_values(sudoku, 0, 2)

print(possible_values)

# TODO Reimplement this functionality in the solver.
#for i in range(9):
#    for j in range(9):
#        possible_values = soduku_solver.get_possible_values(soduku, i, j)
#        if len(possible_values) == 1:
#            soduku.add_cell(i, j, possible_values[0])
#
#soduku.print_board()