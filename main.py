import board as b
import tkinter as tk
import timer
def play():
    play_button.destroy()## destroy button
    board = b.Board(root)
    board.place(x=300, y=200)
    b.Board.show_total_number(root)
    time = timer.Count_time(root)
root = tk.Tk()
root.title('OTHELLO !')
root.geometry('1000x700')
title = tk.Label(root,text="OTHELLO !!!",font=('arial',40))#title of the game
title.place(x=350, y=10)
play_button = tk.Button(root,text='Player VS player',command=play,width=20,height=5,bg='green')
play_button.pack(padx=200,pady=100)
root.mainloop()