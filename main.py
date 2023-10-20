import board as b
import tkinter as tk
import blackbotboard as bb
import white_bot
def player_vs_player():#player vs player 
    pvp_button.destroy()
    bot_button.destroy()
    wbot_button.destroy()
    board = b.Board(root)
    board.place(x=300, y=80)
    board.configure(bg='lightgray')
def player_vs_bot():#player vs black bot
    bot_button.destroy()
    pvp_button.destroy()
    wbot_button.destroy()
    board = bb.Blackbotboard(root)
    board.place(x=300, y=80)
    board.configure(bg='lightgray')
def player_vs_white_bot():
    pvp_button.destroy()
    bot_button.destroy()
    wbot_button.destroy()
    board = white_bot.white_bot(root)
    board.place(x=300, y=80)
    board.configure(bg='lightgray')
root = tk.Tk()
root.title('OTHELLO !')
root.geometry('1000x700')
title = tk.Label(root,text='OTHELLO!!!',font=("Arial", 40))
title.pack()
pvp_button = tk.Button(root,text='Player VS player',command=player_vs_player,width=20,height=5,bg='green')
pvp_button.place(x=450,y=100)
bot_button = tk.Button(root,text='Player VS black Bot',command=player_vs_bot,width=20,height=5,bg='green')
bot_button.place(x=450,y=200)
wbot_button = tk.Button(root,text='Player VS white Bot',command=player_vs_white_bot,width=20,height=5,bg='green')
wbot_button.place(x=450,y=300)
root.mainloop()
