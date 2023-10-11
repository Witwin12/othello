import tkinter as tk

class Board(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_table()
    def create_table(self):
        for i in range(8):
            for j in range(8):
                if (i == 3 and j == 3) or (i == 4 and j ==4):
                    each = tk.Button(self, bg = 'white', padx=19, pady=12, relief="solid", command=lambda i=i, j=j: self.send(i, j))
                    each.grid(row=i, column=j)
                elif (i == 3 and j == 4) or (i == 4 and j == 3):
                    each = tk.Button(self, bg = 'black', padx=19, pady=12, relief="solid", command=lambda i=i, j=j: self.send(i, j))
                    each.grid(row=i, column=j)
                else:
                    picture_1 = tk.PhotoImage(file='each_table.png')
                    each = tk.Button(self, image= picture_1, padx=20, pady=20, relief="solid", command=lambda i=i, j=j: self.send(i, j))
                    each.grid(row=i, column=j)
                    each.image = picture_1


    
    def send(self, i, j):
        self.i = i
        self.j = j
        