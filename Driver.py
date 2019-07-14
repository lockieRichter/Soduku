import fileinput

from soduku_board import Soduku


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

board = read_board_in()

soduku = Soduku(board)

print("You entered the following board..")
soduku.print_board()
print("Is that correct? (yes/no)")
