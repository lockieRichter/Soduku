import numpy
from numpy import array
from typing import List


class Sudoku:

    def __init__(self, board: List[int]) -> None:
        self.board = array(board)

    def print_board(self) -> None:
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

    def add_cell(self, row: int, column: int, value: int) -> None:
        self.board[row][column] = value

    def get_box(self, row: int, column: int) -> numpy.ndarray:
        if row // 3 == 0:
            box = self.board[0:3, :]
        elif row // 3 == 1:
            box = self.board[3:6, :]
        elif row // 3 == 2:
            box = self.board[6:9, :]

        if column // 3 == 0:
            box = box[:, 0:3]
        elif column // 3 == 1:
            box = box[:, 3:6]
        elif column // 3 == 2:
            box = box[:, 6:9]

        return box
