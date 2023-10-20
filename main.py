import board as b
import tkinter as tk
import blackbotboard as bb
import white_bot

# Declare board and game_started as global variables
board = None
menu_button = None
def player_vs_player():
    global board,menu_button
    pvp_button.destroy()
    bot_button.destroy()
    wbot_button.destroy()
    board = b.Board(root)
    board.place(x=300, y=80)
    board.configure(bg='lightgray')
    menu_button = tk.Button(root, text='Main Menu', command=main_menu, width=20, height=5, bg='green')
    menu_button.place(x=100, y=100)

def player_vs_bot():
    global board,menu_button
    bot_button.destroy()
    pvp_button.destroy()
    wbot_button.destroy()
    board = bb.Blackbotboard(root)
    board.place(x=300, y=80)
    board.configure(bg='lightgray')
    menu_button = tk.Button(root, text='Main Menu', command=main_menu, width=20, height=5, bg='green')
    menu_button.place(x=100, y=100)

def player_vs_white_bot():
    global board,menu_button
    pvp_button.destroy()
    bot_button.destroy()
    wbot_button.destroy()
    board = white_bot.white_bot(root)
    board.place(x=300, y=80)
    board.configure(bg='lightgray')
    menu_button = tk.Button(root, text='Main Menu', command=main_menu, width=20, height=5, bg='green')
    menu_button.place(x=100, y=100)

def main_menu():
    global board,menu_button
    if board:
        board.destroy()
        board = None
    pvp_button = tk.Button(root, text='Player VS player', command=player_vs_player, width=20, height=5, bg='green')
    pvp_button.place(x=450, y=100)
    bot_button = tk.Button(root, text='Player VS black Bot', command=player_vs_bot, width=20, height=5, bg='green')
    bot_button.place(x=450, y=200)
    wbot_button = tk.Button(root, text='Player VS white Bot', command=player_vs_white_bot, width=20, height=5, bg='green')
    wbot_button.place(x=450, y=300)
    menu_button.destroy()

root = tk.Tk()
root.title('OTHELLO!')
root.geometry('1000x700')
title = tk.Label(root, text='OTHELLO!!!', font=("Arial", 40))
title.pack()

pvp_button = tk.Button(root, text='Player VS player', command=player_vs_player, width=20, height=5, bg='green')
pvp_button.place(x=450, y=100)
bot_button = tk.Button(root, text='Player VS black Bot', command=player_vs_bot, width=20, height=5, bg='green')
bot_button.place(x=450, y=200)
wbot_button = tk.Button(root, text='Player VS white Bot', command=player_vs_white_bot, width=20, height=5, bg='green')
wbot_button.place(x=450, y=300)

root.mainloop()
