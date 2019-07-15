from numpy import unique
from numpy import array


def verify_row(soduku, row):
    row_values = soduku.board[row][:]
    if len(row_values) > len(set(row_values)):
        return False
    else:
        return True


def verify_column(soduku, column):
    column_values = soduku.board[:][column]
    if len(column_values) > len(set(column_values)):
        return False
    else:
        return True


def verify_box(soduku, box):
    d = box // 3
    r = box % 3
    box_values = None

    if d == 0:
        box_values = soduku.board[:, :3]
    elif d == 1:
        box_values = soduku.board[:, 3:6]
    elif d == 2:
        box_values = soduku.board[:, 6:]

    if r == 0:
        box_values = box_values[:3, :]
    elif r == 1:
        box_values = box_values[3:6, :]
    elif r == 2:
        box_values = box_values[6:, :]

    if len(unique(box_values)) != 9:
        return False
    else:
        return True


def verify_board(soduku):
    for i in range(9):
        if not (verify_row(soduku, i) and verify_column(soduku, i) and verify_box(soduku, i)):
            return False
        else:
            return True


def non_zero(value):
    if value != 0:
        return True
    else:
        return False


def get_possible_values(soduku, row, column):
    all_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    possible_values = []

    row_values = array(list(filter(non_zero, soduku.board[row, :]))).flatten()
    column_values = array(list(filter(non_zero, soduku.board[:, column]))).flatten()

    if row % 3 == 0:
        box = soduku.board[0:3, :]
    elif row % 3 == 1:
        box = soduku.board[4:6, :]
    elif row % 3 == 2:
        box = soduku.board[7:9, :]

    if column % 3 == 0:
        box = box[:, 0:3]
    elif column % 3 == 1:
        box = box[:, 4:6]
    elif column % 3 == 2:
        box = box[:, 7:9]

    box_values = list(filter(non_zero, array(list(box)).flatten()))

    #TODO Need to verify these values.


