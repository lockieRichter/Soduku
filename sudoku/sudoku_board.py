from typing import List

import numpy
from numpy import array


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

    def get_box_from_cell(self, row: int, column: int) -> numpy.ndarray:
        box = None
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

    def get_box_from_index(self, box_number: int) -> numpy.ndarray:
        box = None
        if box_number == 0:
            box = self.get_box_from_cell(0, 0)
        elif box_number == 1:
            box = self.get_box_from_cell(0, 4)
        elif box_number == 2:
            box = self.get_box_from_cell(0, 8)
        elif box_number == 3:
            box = self.get_box_from_cell(4, 0)
        elif box_number == 4:
            box = self.get_box_from_cell(4, 4)
        elif box_number == 5:
            box = self.get_box_from_cell(4, 8)
        elif box_number == 6:
            box = self.get_box_from_cell(8, 0)
        elif box_number == 7:
            box = self.get_box_from_cell(8, 4)
        elif box_number == 8:
            box = self.get_box_from_cell(8, 8)

        return box
