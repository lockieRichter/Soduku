import tkinter as tk
from typing import List

import numpy
from numpy import array

from time import sleep


class Sudoku:

    def __init__(self, board: List[int], gui: tk.Tk = None) -> None:
        self.board_numbers = array(board)
        self.gui = gui

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
                print('', self.board_numbers[i][j], end='')
            print(' |')
        print('  -----------------------')

    def add_cell(self, row: int, column: int, value: int) -> None:
        self.board_numbers[row][column] = value
        if self.gui is not None:
            self.gui.add_value_to_gui(row, column, value)
            sleep(0.02)
            self.gui.window.update()

    def get_box_from_cell(self, row: int, column: int) -> numpy.ndarray:
        box = None
        if row // 3 == 0:
            box = self.board_numbers[0:3, :]
        elif row // 3 == 1:
            box = self.board_numbers[3:6, :]
        elif row // 3 == 2:
            box = self.board_numbers[6:9, :]

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
