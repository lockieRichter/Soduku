import fileinput

from Soduku import Soduku


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

valid_board = [[2, 4, 8, 3, 9, 5, 7, 1, 6],
               [5, 7, 1, 6, 2, 8, 3, 4, 9],
               [9, 3, 6, 7, 4, 1, 5, 8, 2],
               [6, 8, 2, 5, 3, 9, 1, 7, 4],
               [3, 5, 9, 1, 7, 4, 6, 2, 8],
               [7, 1, 4, 8, 6, 2, 9, 5, 3],
               [8, 6, 3, 4, 1, 7, 2, 9, 5],
               [1, 9, 5, 2, 8, 6, 4, 3, 7],
               [4, 2, 7, 9, 5, 3, 8, 6, 1]]

soduku = Soduku(valid_board)

print("You entered the following board..")
soduku.print_board()
print("Is that correct? (yes/no)")

soduku.verify_box(0)
