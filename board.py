import tkinter as tk
from tkinter import messagebox
from setting import Setting
from time_widget import Time_widget


class Board(tk.Frame):
    def __init__(self, master):
        super().__init__(master,bg='light gray')
        self.load_piece_images()
        self.create_table()
        self.create_hint()
        self.initialize_game()
        self.update_board()
        self.hinter()
        self.show_player()
        self.create_total_score()
        self.time_widget = Time_widget(self)  # Create a Time_widget instance
        self.time_widget.grid(row=13,column=1, columnspan=6, pady= 10)  # Display the Time_widget label on your board
        self.reset_widget()
        self.re_widget.place(x=50,y=525)
    
    def create_table(self):
        self.buttons = []
        # Create column labels (A, B, C, ...)
        for j in range(8):
            label = tk.Label(self, text=chr(ord('A') + j), font=("Arial", 12),bg='lightgray')
            label.grid(row=8, column=j, pady=5)
        for i in range(8):
            row = []
                # Create row label (1, 2, 3, ...)
            row_label = tk.Label(self, text=str(i + 1), font=("Arial", 12),bg='lightgray')
            row_label.grid(row=i, column=8, padx=5)
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
                messagebox.showinfo('Attention please!','The game have to swap player.')
                print('swap player')
                self.clear_hint()
                self.current_player = 3 - self.current_player
                self.hinter()

        self.fixed_show_player()
        self.update_score()

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
            self.time_widget.flag = False
            messagebox.showinfo('End Game!',self.setting.determine_winner()+ f'\nTime: [{self.time_widget.timeHour:02d}:{self.time_widget.timeMin:02d}:{self.time_widget.timeSec:02d}]')
            self.time_widget.flag = True
            self.time_widget.update_time()

            self.setting.table_matrix = [[0, 0, 0, 0, 0, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 0, 0, 0],
                                         [0, 0, 0, 2, 1, 0, 0, 0],
                                         [0, 0, 0, 1, 2, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 0, 0, 0]]
            self.update_board()
            self.current_player = 1
            self.hinter()
            self.update_score()
            self.time_widget.reset_time()

    def show_player(self):
        self.player_widget = tk.Label(self, text= 'Black turn', font=('Grandview',32), bg='light gray')
        self.picture_piecce = tk.Label(self, image=self.black_piece_image)
        self.picture_piecce.grid(row=9,column=0, columnspan=2)
        self.player_widget.grid(row=9,column=1, columnspan= 6, pady= 10)
    
    def fixed_show_player(self):
        if self.current_player == 1:
            self.player_widget.configure(text= 'Black turn')
            self.picture_piecce.configure(image=self.black_piece_image)
        else:
            self.player_widget.configure(text= 'White turn')
            self.picture_piecce.configure(image=self.white_piece_image)

    def create_total_score(self):
        self.player1_show_score = tk.Label(self,text='Black score: 2', bg='light gray', font=('Grandview',12))
        self.player1_show_score.grid(row=10,column=0,columnspan=8, pady= 10)
        self.player2_show_score = tk.Label(self,text='White score: 2', bg='light gray', font=('Grandview',12))
        self.player2_show_score.grid(row=12,column=0,columnspan=8, pady= 10)

    def update_score(self):
        self.player1_score = sum(row.count(1) for row in self.setting.table_matrix)
        self.player2_score = sum(row.count(2) for row in self.setting.table_matrix)
        self.player1_show_score.configure(text=f'Black score: {self.player1_score}')
        self.player2_show_score.configure(text=f'White score: {self.player2_score}')

    def reset(self):

            self.setting.table_matrix = [[0, 0, 0, 0, 0, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 0, 0, 0],
                                         [0, 0, 0, 2, 1, 0, 0, 0],
                                         [0, 0, 0, 1, 2, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 0, 0, 0]]
            self.update_board()
            self.current_player = 1
            self.update_score()
            self.time_widget.reset_time()
            self.clear_hint()
            self.hinter()

    def reset_widget(self):
        self.re_widget = tk.Button(self, text='Reset', bg='light gray', font=('Grandview',12),activebackground='red')
        self.re_widget.configure(command=lambda: self.reset())