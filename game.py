import board as b
import tkinter as tk

root = tk.Tk()
root.title('OTHELLO !')
root.geometry('500x500')

board = b.Board(root)
board.place(x=50, y=50)

t = tk.Label(board)
t.grid(column=0, row=0)

root.mainloop()