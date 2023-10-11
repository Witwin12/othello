import board as b
import tkinter as tk

root = tk.Tk()
root.title('OTHELLO !')
root.geometry('1000x700')

board = b.Board(root)
board.place(x=50, y=50)

t = tk.Label(board,text='test')
t.grid(column=0, row=0)

root.mainloop()