import main as m
import tkinter as tk
root = tk.Tk()
root.title('OTHELLO !')
root.geometry('1000x700')
play_button = tk.Button(text='Play')
play_button.bind("<ButtonPress-1>",m)
play_button.pack()
root.mainloop()