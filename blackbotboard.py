from board import Board
import random
from tkinter import messagebox
class Blackbotboard(Board):
    def __init__(self, master):
        super().__init__(master)
        self.blackbot_play()
        
    def blackbot_play(self):
        i,j = random.choice(self.setting.find_valid_moves(self.current_player))
        print(f'Go GO {i}, {j}')
        self.setting.place_piece(i,j,self.current_player)
        self.clear_hint()
        self.current_player = 3 - self.current_player
        self.update_board()
        self.hinter()
        self.fixed_show_player()
        self.update_score()
        if len(self.setting.find_valid_moves(self.current_player)) == 0:
                messagebox.showinfo('Attention please!','The game have to swap player.')
                print('swap player')
                self.clear_hint()
                self.current_player = 3 - self.current_player
                self.hinter()
    def send(self, i, j):
        super().send(i, j)
        if self.current_player == 1:
            self.blackbot_play()
            self.show_win()
        

    def show_win(self):
        super().show_win()
        if self.setting.table_matrix == [[0, 0, 0, 0, 0, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 0, 0, 0],
                                         [0, 0, 0, 2, 1, 0, 0, 0],
                                         [0, 0, 0, 1, 2, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 0, 0, 0],
                                         [0, 0, 0, 0, 0, 0, 0, 0]]:
            self.blackbot_play()
    
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
        self.blackbot_play()
        self.update_score()
        self.time_widget.reset_time()
        self.clear_hint()
        self.hinter()