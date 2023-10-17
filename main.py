import board as b
import tkinter as tk
def player_vs_player():
    pvp_button.destroy()
    board = b.Board(root)
    board.place(x=50, y=50)
    board.configure(bg= 'light blue')

root = tk.Tk()
root.title('OTHELLO !')
root.geometry('1000x700')
root.configure(bg='light blue')
pvp_button = tk.Button(root,text='Player VS player',command=player_vs_player,width=20,height=5,bg='green')
pvp_button.pack(padx=200,pady=100)

root.mainloop()