from sudoku import sudoku_solver, boards
from sudoku.sudoku_board import Sudoku
import tkinter as tk


class Gui:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Sudoku Solver")
        self.text_boxes = []
        self.create_board()
        self.solve_button = tk.Button(self.window, text="Solve!", command=self.solve_clicked)
        self.solve_button.grid(row=14, columnspan=13)

    def run(self):
        self.window.mainloop()

    def create_board(self):
        for row in range(13):
            if row % 4 == 0:
                for column in range(13):
                    txt = tk.Label(self.window, text="-")
                    txt.grid(row=row, column=column)
            else:
                row_boxes = []
                for column in range(13):
                    if column % 4 == 0:
                        txt = tk.Label(self.window, text="|")
                    else:
                        txt = tk.Entry(self.window, width=1)
                        row_boxes.append(txt)

                    txt.grid(row=row, column=column)
                self.text_boxes.append(row_boxes)

    def solve_clicked(self):
        print("Solve button clicked.")
        board = boards.empty
        self.solve_button.config(state='disabled')

        for row in range(9):
            for column in range(9):
                current_box = self.text_boxes[row][column]
                if str.isdigit(current_box.get()) and len(current_box.get()) == 1:
                    current_box.config(state='disabled')
                    board[row][column] = int(current_box.get())

        sudoku = Sudoku(board, self)
        sudoku_solver.solve_board(sudoku)

    def add_value_to_gui(self, row: int, column: int, value: int):
        self.text_boxes[row][column].delete(0, tk.END)
        if value != 0:
            self.text_boxes[row][column].insert(0, value)