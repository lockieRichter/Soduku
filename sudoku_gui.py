from sudoku import sudoku_solver, boards
from sudoku.sudoku_board import Sudoku
import tkinter as tk


def solve_clicked():
    print("Solve button clicked.")
    board = boards.empty;
    for row in range(9):
        for column in range(9):
            if str.isdigit(text_boxes[row][column].get()) and len(text_boxes[row][column].get()) == 1:
                text_boxes[row][column].config(state='disabled')
                board[row][column] = int(text_boxes[row][column].get())

    sudoku = Sudoku(board, True)
    sudoku_solver.solve_board(sudoku)


def create_board():
    for row in range(13):
        if row % 4 == 0:
            for column in range(13):
                txt = tk.Label(window, text="-")
                txt.grid(row=row, column=column)
        else:
            row_boxes = []
            for column in range(13):
                if column % 4 == 0:
                    txt = tk.Label(window, text="|")
                else:
                    txt = tk.Entry(window, width=1)
                    row_boxes.append(txt)

                txt.grid(row=row, column=column)
            text_boxes.append(row_boxes)


window = tk.Tk()
window.title("Sudoku Solver")
text_boxes = []
create_board()

solve_button = tk.Button(window, text="Solve!", command=solve_clicked)
solve_button.grid(row=14, columnspan=13)

window.mainloop()
