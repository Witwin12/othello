import tkinter as tk
from tkinter import PhotoImage
from board import Board
import blackbotboard as bb
import white_bot as wb
from bot_vs_bot import Botvsbot

class Buttonmenu(tk.Button):
    def __init__(self, master, board, frame):
        super().__init__(master, bg='light pink', borderwidth=5, relief=tk.RIDGE)
        self.board = board
        self.frame = frame
        self.configure(command=self.open_thatframe)

    def open_thatframe(self):
        bvb.gamestate = False
        for frame in frames:
            frame.pack_forget()  # Hide all frames
        self.board.reset()
        self.board.pack(in_=self.frame)

class Newbuttonmenu(Buttonmenu):
    def __init__(self, master, board, frame):
        super().__init__(master, board, frame)

    def open_thatframe(self):
        super().open_thatframe()
        self.board.gamestate = True

############# use for home button ###################
def Home():
    global flag
    bvb.gamestate = False
    bot_frame.place_forget()
    option_frame.place(x=0,y=0)
    for frame in frames:
        frame.pack_forget()
    flag = False
        
def bot():# change a frame to bot frame
    global flag
    flag = True
    if flag:
        option_frame.pack_forget()
        bot_frame.place(x=0,y=0)
    for frame in frames:
        frame.pack_forget()
    bvb.gamestate = False
root = tk.Tk()
root.title('Othello')
root.geometry('600x600')

flag = False
bg_image = PhotoImage(file='bg_option.png')

option_frame = tk.Frame(root, borderwidth=5, relief=tk.RIDGE)
option_frame.place(x=0,y=0)
option_frame.configure(width=200, height=600)

# ใช้ Label แสดงรูปภาพใน option_frame
option_label = tk.Label(option_frame, image=bg_image)
option_label.place(relwidth=1, relheight=1)  # ทำให้รูปเต็มพื้นที่ของ option_frame

bg_g_image = PhotoImage(file='bg_game.png')

game_frame = tk.Frame(root)
game_frame.configure(width=400, height=600)
game_frame.place(x=205,y=0)
game_label = tk.Label(game_frame, image= bg_g_image)
game_label.place(relwidth=1, relheight=1)

bot_frame = tk.Frame(root,borderwidth=5, relief=tk.RIDGE)
bot_frame.configure(width=200,height=600)
bot_label = tk.Label(bot_frame,image=bg_image)
bot_label.place(relwidth=1,relheight=1)

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
pvp_button.place(y= 120, x=30)
frames.append(pvp)

# button PVWB
pvwb = wb.normal_white_bot(game_frame)
pvwb_button = Buttonmenu(bot_frame, pvwb, game_frame)
pvwb_button.configure(text='Player vs Normal Bot', font=('Forte',12), borderwidth=5, relief=tk.RIDGE)
pvwb_button.place(y= 220, x=10)
frames.append(pvwb)

# button BBVP
bbvp = bb.Blackbotboard(game_frame)
bbvp_button = Buttonmenu(bot_frame, bbvp, game_frame)
bbvp_button.configure(text='easy Bot vs Player', font=('Forte',12), borderwidth=5, relief=tk.RIDGE)
bbvp_button.place(y= 320, x=10)
frames.append(bbvp)

# Home
home_button = tk.Button(option_frame, text='Home', font=('Forte',12), bg='light pink', borderwidth=5, relief=tk.RIDGE)
home_button.place(y= 20, x=30)
home_button.configure(command=Home)
#new Home
new_home_button = tk.Button(bot_frame, text='Home', font=('Forte',12), bg='light pink', borderwidth=5, relief=tk.RIDGE,command=Home)
new_home_button.place(y= 20, x=30)

# button BVB
bvb = Botvsbot(game_frame)
bvb_button = Newbuttonmenu(option_frame, bvb, game_frame)
bvb_button.configure(text='Bot vs Bot', font=('Forte',12), borderwidth=5, relief=tk.RIDGE)
bvb_button.place(y= 370, x=40)
frames.append(bvb)
#p vs easy bot
pvwb = wb.easy_white_bot(game_frame)
pvwb_button = Buttonmenu(bot_frame, pvwb, game_frame)
pvwb_button.configure(text='Player vs Easy Bot', font=('Forte',12), borderwidth=5, relief=tk.RIDGE)
pvwb_button.place(y= 170, x=10)
frames.append(pvwb)
#p vs hard bot
pvwb = wb.hard_white_bot(game_frame)
pvwb_button = Buttonmenu(bot_frame, pvwb, game_frame)
pvwb_button.configure(text='Player vs Hard Bot', font=('Forte',12), borderwidth=5, relief=tk.RIDGE)
pvwb_button.place(y= 270, x=10)
frames.append(pvwb)
#bot button
bot_button = tk.Button(option_frame,text='vs Bot', font=('Forte',12), borderwidth=5, relief=tk.RIDGE,command=bot,bg = 'light pink')
bot_button.place(y=250,x=50)
# normal bb vs p button
bbvp = bb.normal_black_bot(game_frame)
bbvp_button = Buttonmenu(bot_frame, bbvp, game_frame)
bbvp_button.configure(text='Normal Bot vs Player', font=('Forte',12), borderwidth=5, relief=tk.RIDGE)
bbvp_button.place(y= 370, x=10)
frames.append(bbvp)
# hard bb vs p button
bbvp = bb.hard_black_bot(game_frame)
bbvp_button = Buttonmenu(bot_frame, bbvp, game_frame)
bbvp_button.configure(text='hard Bot vs Player', font=('Forte',12), borderwidth=5, relief=tk.RIDGE)
bbvp_button.place(y= 420, x=10)
frames.append(bbvp)
root.mainloop()
