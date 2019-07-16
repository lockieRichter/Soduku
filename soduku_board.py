from numpy import array


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

    def add_cell(self, row, column, value):
        self.board[row][column] = value

    def get_box(self, row, column):
        if row % 3 == 0:
            box = self.board[0:3, :]
        elif row % 3 == 1:
            box = self.board[4:6, :]
        elif row % 3 == 2:
            box = self.board[7:9, :]

        if column % 3 == 0:
            box = box[:, 0:3]
        elif column % 3 == 1:
            box = box[:, 4:6]
        elif column % 3 == 2:
            box = box[:, 7:9]

        return box
