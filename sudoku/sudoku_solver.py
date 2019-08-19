from itertools import chain
from typing import List

from numpy import unique

from sudoku import sudoku_board

is_cli = False


def verify_row(sudoku: sudoku_board.Sudoku, row: int) -> bool:
    row_values = sudoku.board_numbers[row][:]
    return len(row_values) <= len(set(row_values)) and 0 not in row_values


def verify_column(sudoku: sudoku_board.Sudoku, column: int) -> bool:
    column_values = sudoku.board_numbers[:][column]
    return len(column_values) <= len(set(column_values)) and 0 not in column_values


def verify_box(sudoku: sudoku_board.Sudoku, box: int) -> bool:
    d = box // 3
    r = box % 3
    box_values = None

    if d == 0:
        box_values = sudoku.board_numbers[:, :3]
    elif d == 1:
        box_values = sudoku.board_numbers[:, 3:6]
    elif d == 2:
        box_values = sudoku.board_numbers[:, 6:]

    if r == 0:
        box_values = box_values[:3, :]
    elif r == 1:
        box_values = box_values[3:6, :]
    elif r == 2:
        box_values = box_values[6:, :]

    return len(unique(box_values)) == 9 and 0 not in box_values


def verify_board(sudoku: sudoku_board.Sudoku) -> bool:
    for i in range(9):
        if not (verify_row(sudoku, i) and verify_column(sudoku, i) and verify_box(sudoku, i)):
            return False
    return True


def non_zero(value: int) -> bool:
    return value != 0


def get_possible_cell_values(sudoku: sudoku_board.Sudoku, row: int, column: int) -> List[int]:
    all_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    possible_values = []

    if sudoku.board_numbers[row][column] != 0:
        possible_values.append(sudoku.board_numbers[row][column])
    else:
        row_values = sudoku.board_numbers[row, :].flatten()
        column_values = sudoku.board_numbers[:, column].flatten()
        box_values = sudoku.get_box_from_cell(row, column).flatten()

        used_values = unique(list(filter(non_zero, chain(row_values, column_values, box_values))))

        for value in all_values:
            if value not in used_values:
                possible_values.append(value)

    return possible_values


def solve_all_single_value_cells(sudoku: sudoku_board.Sudoku) -> None:
    solved_value = True
    while solved_value:
        solved_value = False
        for row in range(9):
            for column in range(9):
                values = get_possible_cell_values(sudoku, row, column)
                if len(values) == 1 and sudoku.board_numbers[row][column] == 0:
                    sudoku.add_cell(row, column, values[0])
                    solved_value = True


def check_row_for_value(sudoku: sudoku_board.Sudoku, row: int, value: int) -> bool:
    return value in sudoku.board_numbers[row, :]


def check_column_for_value(sudoku: sudoku_board.Sudoku, column: int, value: int) -> bool:
    return value in sudoku.board_numbers[:, column]


def get_rows_from_box_index(box_number: int) -> List[int]:
    rows = []
    if 0 <= box_number < 3:
        rows = [0, 1, 2]
    elif 3 <= box_number < 6:
        rows = [3, 4, 5]
    elif 6 <= box_number < 9:
        rows = [6, 7, 8]

    return rows


def get_columns_from_box_index(box_number: int) -> List[int]:
    columns = []
    if box_number % 3 == 0:
        columns = [0, 1, 2]
    elif box_number % 3 == 1:
        columns = [3, 4, 5]
    elif box_number % 3 == 2:
        columns = [6, 7, 8]

    return columns


def crosshatch_box(sudoku: sudoku_board.Sudoku, box_number: int) -> bool:
    all_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    unused_values = []

    box = sudoku.get_box_from_index(box_number)
    box_values = box.flatten()

    for value in all_values:
        if value not in box_values:
            unused_values.append(value)

    solved_value = False
    # Loop through each value that is not in the box.
    for value in unused_values:
        possible_rows = []
        possible_columns = []

        # Check each row that goes through the box.
        for row in get_rows_from_box_index(box_number):
            # If the value is not in that row then it could be in that row of the box.
            if not check_row_for_value(sudoku, row, value):
                possible_rows.append(row)
        # Check each column that goes through the box.
        for column in get_columns_from_box_index(box_number):
            # If the value is not in that column then it could be in that column of the box.
            if not check_column_for_value(sudoku, column, value):
                possible_columns.append(column)

        # Remove duplicates from possible rows and columns.
        possible_rows = list(set(possible_rows))
        possible_columns = list(set(possible_columns))

        # A cell position is only possible if the value is 0. Save the index if it is.
        possible_index = []
        for row in possible_rows:
            for column in possible_columns:
                if sudoku.board_numbers[row, column] == 0:
                    possible_index.append([row, column])

        # If there is only one possible value for this cell then add it to the board.
        if len(possible_index) == 1:
            sudoku.board_numbers[possible_index[0][0], possible_index[0][1]] = value
            solved_value = True

    return solved_value


def solve_all_crosshatch_boxes(sudoku: sudoku_board.Sudoku) -> None:
    solved_value = True
    while solved_value:
        solved_value = False
        for box_number in range(9):
            solved_value = crosshatch_box(sudoku, box_number)


def solve_all_naked_subsets(sudoku: sudoku_board.Sudoku):
    for index in range(9):
        solve_naked_subset_row(sudoku, index)
        solve_naked_subset_column(sudoku, index)


# For each empty cell in a column, if there are n possible numbers that can only appear in n separate cells,
# then these numbers can be removed from the other cells as possibilities.
def solve_naked_subset_column(sudoku: sudoku_board.Sudoku, column: int) -> None:
    cell_possible_values = []
    for row in range(9):
        cell_possible_values.append(get_possible_cell_values(sudoku, row, column))

    subset_indices_two = []
    for cell in range(9):
        if len(cell_possible_values[cell]) == 2:
            subset_indices_two.append(cell)

    values_two = []
    if len(subset_indices_two) == 2:
        values_two = cell_possible_values[subset_indices_two[0]]

    for index in range(9):
        if index not in subset_indices_two:
            cell_possible_values[index] = (list(set(cell_possible_values[index]) - set(values_two)))

    for row in range(9):
        if len(cell_possible_values[row]) == 1:
            sudoku.board_numbers[row, column] = cell_possible_values[row][0]


def solve_naked_subset_row(sudoku: sudoku_board.Sudoku, row: int) -> None:
    cell_possible_values = []
    for column in range(9):
        cell_possible_values.append(get_possible_cell_values(sudoku, row, column))

    subset_indices_two = []
    for cell in range(9):
        if len(cell_possible_values[cell]) == 2:
            subset_indices_two.append(cell)

    values_two = []
    if len(subset_indices_two) == 2:
        values_two = cell_possible_values[subset_indices_two[0]]

    for index in range(9):
        if index not in subset_indices_two:
            cell_possible_values[index] = (list(set(cell_possible_values[index]) - set(values_two)))

    for column in range(9):
        if len(cell_possible_values[column]) == 1:
            sudoku.board_numbers[row, column] = cell_possible_values[column][0]


# Function to Find the entry in the Grid that is still  not used
# Searches the grid to find an entry that is still unassigned. If
# found, the reference parameters row, col will be set the location
# that is unassigned, and true is returned. If no unassigned entries
# remain, false is returned.
# 'l' is a list  variable that has been passed from the solve_sudoku function
# to keep track of incrementation of Rows and Columns
def find_empty_location(arr, l):
    for row in range(9):
        for col in range(9):
            if arr[row][col] == 0:
                l[0] = row
                l[1] = col
                return True
    return False


# Returns a boolean which indicates whether any assigned entry
# in the specified row matches the given number.
def used_in_row(arr, row, num):
    for i in range(9):
        if arr[row][i] == num:
            return True
    return False


# Returns a boolean which indicates whether any assigned entry
# in the specified column matches the given number.
def used_in_col(arr, col, num):
    for i in range(9):
        if arr[i][col] == num:
            return True
    return False


# Returns a boolean which indicates whether any assigned entry
# within the specified 3x3 box matches the given number
def used_in_box(arr, row, col, num):
    for i in range(3):
        for j in range(3):
            if arr[i + row][j + col] == num:
                return True
    return False


# Checks whether it will be legal to assign num to the given row,col
#  Returns a boolean which indicates whether it will be legal to assign
#  num to the given row,col location.
def check_location_is_safe(arr, row, col, num):
    # Check if 'num' is not already placed in current row,
    # current column and current 3x3 box
    return not used_in_row(arr, row, num) and not used_in_col(arr, col, num) and not used_in_box(arr, row - row % 3,
                                                                                                 col - col % 3, num)


# Takes a partially filled-in grid and attempts to assign values to
# all unassigned locations in such a way to meet the requirements
# for Sudoku solution (non-duplication across rows, columns, and boxes)
def brute_force_solve_sudoku(arr):
    # 'l' is a list variable that keeps the record of row and col in find_empty_location Function
    location = [0, 0]

    # If there is no unassigned location, we are done
    if not find_empty_location(arr, location):
        return True

    # Assigning list values to row and col that we got from the above Function
    row = location[0]
    col = location[1]

    # consider digits 1 to 9
    for num in range(1, 10):

        # if looks promising
        if check_location_is_safe(arr, row, col, num):

            # make tentative assignment
            arr[row][col] = num

            # return, if success, ya!
            if brute_force_solve_sudoku(arr):
                return True

            # failure, unmake & try again
            arr[row][col] = 0

    # this triggers backtracking
    return False


def solve_board(sudoku: sudoku_board.Sudoku):
    iterations = 0
    while not verify_board(sudoku):
        iterations += 1
        solve_all_single_value_cells(sudoku)
        solve_all_crosshatch_boxes(sudoku)
        solve_all_naked_subsets(sudoku)

        if iterations == 20:
            if is_cli:
                print("Could not find a solution after 20 iterations.")
                print("Have solved the board to the following point...")
                sudoku.print_board()
                print("Will now try to brute force solve the board...")
            brute_force_solve_sudoku(sudoku.board_numbers)

    if verify_board(sudoku):
        if is_cli:
            print("Have completed the board with the following solution, after {0} iterations...".format(iterations))
            sudoku.print_board()
        return


def set_is_cli(cli: bool):
    global is_cli
    is_cli = cli
