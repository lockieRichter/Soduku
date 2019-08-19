from sudoku import sudoku_solver, boards
from sudoku.sudoku_board import Sudoku
import tkinter as tk


def get_board():
    board_values = boards.empty
    for r in range(9):
        for c in range(9):
            val = text_boxes[r][c].get()
            if val != '' and len(val) == 1 and str.isdigit(val):
                board_values[r][c] = text_boxes[r][c].get()
    return board_values


def solve_pressed():
    btn['state'] = 'disabled'
    sudoku_board = Sudoku(get_board())
    sudoku_solver.set_is_cli(False)
    sudoku_solver.solve_board(sudoku_board)


window = tk.Tk()
window.title("Sudoku")
lbl = tk.Label(window, text="Hello")
lbl.grid(column=10, row=10)
text_boxes = []
for row in range(9):
    row_values = []
    for column in range(9):
        txt = tk.Entry(window, width=1)
        txt.grid(column=column, row=row)
        row_values.append(txt)
    text_boxes.append(row_values)

btn = tk.Button(window, text="Solve", command=solve_pressed)
btn.grid(column=11, row=10)

window.mainloop()
