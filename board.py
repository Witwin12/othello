import tkinter as tk
from tkinter import messagebox
from setting import Setting
class Board(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.load_piece_images()
        self.create_table()
        self.create_hint()
        self.initialize_game()
        self.update_board()
        self.hinter()
    def create_table(self):
        self.buttons = []
        for i in range(8):
            row = []
            for j in range(8):
                each = tk.Button(self, image= self.each_table_image, padx=20, pady=20, relief="solid", command=lambda i=i, j=j: self.send(i, j))
                each.grid(row=i, column=j)
                row.append(each)
            self.buttons.append(row)

    def initialize_game(self):
        self.setting = Setting()  # สร้างอ็อบเจกต์ Setting สำหรับเกม
        self.current_player = 1  # รายชื่อผู้เล่นรายแรก
    
    def load_piece_images(self):
        self.black_piece_image = tk.PhotoImage(file='black_piece.png')
        self.white_piece_image = tk.PhotoImage(file='white_piece.png')
        self.each_table_image = tk.PhotoImage(file='each_table.png')


    def send(self, i, j):

        if self.setting.is_valid_move(i, j, self.current_player):
            self.setting.place_piece(i, j, self.current_player)
            self.update_board()
            print('\n')
            self.clear_hint()
            self.setting.display_board()
            self.current_player = 3 - self.current_player # สลับผู้เล่น
            self.hinter()
        self.show_win()

        if len(self.setting.find_valid_moves(self.current_player)) == 0:
                print('swap plaer')
                self.clear_hint()
                self.current_player = 3 - self.current_player
                self.hinter()

    def update_board(self):
        table_matrix = self.setting.table_matrix
        for i in range(8):
            for j in range(8):
                if table_matrix[i][j] == 1:
                    self.buttons[i][j].configure(image=self.black_piece_image)
                elif table_matrix[i][j] == 2:
                    self.buttons[i][j].configure(image=self.white_piece_image)
                elif table_matrix[i][j] ==0:
                    self.buttons[i][j].configure(image= self.each_table_image)
    
    def create_hint(self):
        self.hints = []
        for i in range(8):
            row = []
            for j in range(8):
                hint = tk.Button(self, bg='light blue', text= '+', fg='blue' )
                hint.configure(command=lambda i=i, j=j: self.send(i, j))
                hint.grid(row=i, column=j)
                row.append(hint)
            self.hints.append(row)
        self.clear_hint()
    
    def clear_hint(self):
        for i in range(8):
            for j in range(8):
                self.hints[i][j].grid_remove()
    
    def hinter(self):
        valid_moves = self.setting.find_valid_moves(self.current_player)
        print(self.setting.find_valid_moves(self.current_player))
        for i, j in valid_moves:
            self.hints[i][j].grid()
    
    def show_win(self):
        if len(self.setting.find_valid_moves(1)) == 0 and len(self.setting.find_valid_moves(2)) == 0:
            messagebox.showinfo('End Game!',self.setting.determine_winner())

            self.setting.table_matrix = [[0, 0, 0, 0, 0, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 0, 0, 0],
                                         [0, 0, 0, 2, 1, 0, 0, 0],
                                         [0, 0, 0, 1, 2, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 0, 0, 0]]

            self.update_board()
            self.hinter()
            self.time =self.time+1
            return(self.time())
