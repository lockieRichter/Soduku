from numpy import array
from numpy import unique


class Soduku:

    def __init__(self, board):
        self.board = array(board)

    def print_board(self):
        for i in range(9):
            if i % 3 == 0:
                if i == 0:
                    print('  -----------------------')
                else:
                    print(' |-------+-------+-------|')

            for j in range(9):
                if j % 3 == 0:
                    print(' |', end='')
                print('', self.board[i][j], end='')
            print(' |')
        print('  -----------------------')

    def get_board(self):
        return self.board

    def verify_row(self, row):
        row_values = self.board[row][:]
        if len(row_values) > len(set(row_values)):
            return False
        else:
            return True

    def verify_column(self, column):
        column_values = self.board[:][column]
        if len(column_values) > len(set(column_values)):
            return False
        else:
            return True

    def verify_box(self, box):
        d = box // 3
        r = box % 3
        box_values = None

        if d == 0:
            box_values = self.board[:, :3]
        elif d == 1:
            box_values = self.board[:, 3:6]
        elif d == 2:
            box_values = self.board[:, 6:]

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

    def verify_board(self):
        for i in range(9):
            if not (self.verify_row(i) and self.verify_column(i) and self.verify_box(i)):
                return False
            else:
                return True
