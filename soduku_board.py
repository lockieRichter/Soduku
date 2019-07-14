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
