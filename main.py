import board as b
import tkinter as tk
def play():
    board = b.Board(root)
    board.place(x=50, y=60)
root = tk.Tk()
root.title('OTHELLO !')
root.geometry('1000x700')
title = tk.Label(root,text="OTHELLO",font=('arial',40))
title.pack()
play_button = tk.Button(root,text='Player VS player',command=play,width=10,height=5)
play_button.pack(padx=100,pady=100)
root.mainloop()