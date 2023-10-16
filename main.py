import board as b
import tkinter as tk
def play():
    board = b.Board(root)
    board.place(x=50, y=50)
root = tk.Tk()
root.title('OTHELLO !')
root.geometry('1000x700')
play_button = tk.Button(root,text='Play',command=play)
play_button.pack()
root.mainloop()