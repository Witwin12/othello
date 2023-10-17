import board as b
import tkinter as tk
def player_vs_player():
    pvp_button.destroy()
    board = b.Board(root)
    board.place(x=300, y=80)
    board.configure(bg='lightxgray')
root = tk.Tk()
root.title('OTHELLO !')
root.geometry('1000x700')
title = tk.Label(root,text='OTHELLO!!!',font=("Arial", 40))
title.pack()
pvp_button = tk.Button(root,text='Player VS player',command=player_vs_player,width=20,height=5,bg='green')
pvp_button.pack(padx=200,pady=100)
root.mainloop()