import tkinter as tk
from tkinter import PhotoImage, Canvas
from board import Board
from blackbotboard import Blackbotboard
import white_bot as wb
class Buttonmenu(tk.Button):
    def __init__(self, master, board, frame):
        super().__init__(master, bg='light pink', borderwidth=5, relief=tk.RIDGE)
        self.board = board
        self.frame = frame

        self.configure(command=self.open_thatframe)

    def open_thatframe(self):
        for frame in frames:
            frame.pack_forget()  # Hide all frames

        self.board.reset()
        self.board.pack(in_=self.frame)


############# use for home button ###################
def Home():
    for frame in frames:
        frame.pack_forget()

root = tk.Tk()
root.title('Othello')
root.geometry('600x600')


bg_image = PhotoImage(file='bg_option.png')

option_frame = tk.Frame(root, borderwidth=5, relief=tk.RIDGE)
option_frame.pack(side=tk.LEFT)
option_frame.configure(width=200, height=600)

# ใช้ Label แสดงรูปภาพใน option_frame
option_label = tk.Label(option_frame, image=bg_image)
option_label.place(relwidth=1, relheight=1)  # ทำให้รูปเต็มพื้นที่ของ option_frame

bg_g_image = PhotoImage(file='bg_game.png')

game_frame = tk.Frame(root)
game_frame.configure(width=400, height=600)
game_frame.pack()
game_label = tk.Label(game_frame, image= bg_g_image)
game_label.place(relwidth=1, relheight=1)

############## home widget ###############
title_label = tk.Label(game_frame,text= 'Othello', font=('Forte',50), borderwidth=3, relief=tk.RIDGE, bg='light yellow')
title_label.place(x=80, y=50)

credits_label = tk.Label(game_frame, text='By\nPruek Tanvorakul 6601012610083\nWitthawin Thitichettrakul 6601012610148'
                         , font=('Grandview',14), borderwidth=3, relief=tk.RIDGE, bg='light yellow')
credits_label.place(x=25, y=500)


title_widget = tk.Label()

frames = []
# button PVP
pvp = Board(game_frame)
pvp_button = Buttonmenu(option_frame, pvp, game_frame)
pvp_button.configure(text='Player vs Player', font=('Forte',12), borderwidth=5, relief=tk.RIDGE)
pvp_button.place(y= 120, x=50)
frames.append(pvp)

# button PVWB
pvwb = wb.white_bot(game_frame)
pvwb_button = Buttonmenu(option_frame, pvwb, game_frame)
pvwb_button.configure(text='Player vs Bot', font=('Forte',12), borderwidth=5, relief=tk.RIDGE)
pvwb_button.place(y= 220, x=50)
frames.append(pvwb)

# button BBVP
bbvp = Blackbotboard(game_frame)
bbvp_button = Buttonmenu(option_frame, bbvp, game_frame)
bbvp_button.configure(text='Bot vs Player', font=('Forte',12), borderwidth=5, relief=tk.RIDGE)
bbvp_button.place(y= 320, x=50)
frames.append(bbvp)

# Home
home_buuton = tk.Button(option_frame, text='Home', font=('Forte',12), bg='light pink', borderwidth=5, relief=tk.RIDGE)
home_buuton.place(y= 20, x=50)
home_buuton.configure(command=Home)


root.mainloop()