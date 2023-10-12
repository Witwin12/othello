import tkinter as tk

class Board(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_table()
    def create_table(self):
        for i in range(8):
            for j in range(8):
                picture = tk.PhotoImage(file='each_table.png')
                each = tk.Button(self, image= picture, padx=20, pady=20, relief="solid", command=lambda i=i, j=j: self.send(i, j))
                each.grid(row=i, column=j)
                each.image = picture


    
    def send(self, i, j):
        self.i = i
        self.j = j
        