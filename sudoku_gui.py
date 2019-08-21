from sudoku import sudoku_solver, boards
from sudoku.sudoku_board import Sudoku
import tkinter as tk


def solve_clicked():
    print("Solve button clicked.")
    solve_button['state'] = 'disabled'


window = tk.Tk()
window.title("Sudoku Solver")
window.config
text_boxes = []
for row in range(13):
    if row % 4 == 0:
        for column in range(13):
            txt = tk.Label(window, text="-")
            txt.grid(row=row, column=column)
    else:
        for column in range(13):
            if column % 4 == 0:
                txt = tk.Label(window, text="|")
            else:
                txt = tk.Entry(window, width=1)

            txt.grid(row=row, column=column)

solve_button = tk.Button(window, text="Solve!", command=solve_clicked)
solve_button.grid(row=14, columnspan=13)

window.mainloop()
