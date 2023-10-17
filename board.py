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
        self.show_player()
        self.show_total_number()
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
        self.update_score()
        if len(self.setting.find_valid_moves(self.current_player)) == 0:
                print('swap plaer')
                self.clear_hint()
                self.current_player = 3 - self.current_player
                self.hinter()

        self.fixed_show_player()

    def update_board(self):
        table_matrix = self.setting.table_matrix
        Setting.time = 0
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
            Setting.time = 1
            messagebox.showinfo('End Game!',self.setting.determine_winner())
            self.reset_game()
            
    def reset_game(self):      
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
        self.current_player()
    def show_player(self):
        self.player_widget = tk.Label(self, bg='black', text= 'Black turn', fg='white', font=('Bauhaus 93',32))
        self.player_widget.grid(row=9, columnspan= 8, pady= 10)
    
    def fixed_show_player(self):
        if self.current_player == 1:
            self.player_widget.configure(bg='black', text= 'Black turn', fg='white')
        else:
            self.player_widget.configure(bg='white', text= 'White turn', fg='Black')
    def show_total_number(self):
        self.player1_show_score = tk.Label(self,text=f'black score: {2}')
        self.player1_show_score.grid(row=10,column=1,columnspan=2)
        self.player2_show_score = tk.Label(self,text=f'white score: {2}')
        self.player2_show_score.grid(row=12,column=1,columnspan=2)
    def update_score(self):
        self.player1_score = sum(row.count(1) for row in self.setting.table_matrix)
        self.player2_score = sum(row.count(2) for row in self.setting.table_matrix)
        self.player1_show_score.configure(text=f'black score: {self.player1_score}')
        self.player2_show_score.configure(text=f'white score: {self.player2_score}')