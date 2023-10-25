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

class normal_black_bot(Blackbotboard):
    def __init__(self, master):
        super().__init__(master)

    def blackbot_play(self):
        valid_moves = self.setting.find_valid_moves(self.current_player)
        corner_moves = [(0, 0),(0, 1),(0, 2),(0, 3),(0, 4),(0, 5),(0, 6),(0, 7),
                        (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7), 
                        (7, 0),(7,1),(7,2),(7,3),(7,4),(7,5),(7,6), (7, 7)]

        i, j = None, None  # Initialize i and j
        # Check if any corner move is a valid move and prioritize it
        for move in corner_moves:
            if move in valid_moves:
                i, j = move
                break

        if i is None:  # If no valid corner move, find any valid move
            if valid_moves:
                i, j = random.choice(valid_moves)

        if i is not None:
            self.setting.place_piece(i, j, self.current_player)
            self.clear_hint()
            self.current_player = 3 - self.current_player
            self.update_board()
            self.hinter()
            self.fixed_show_player()
            self.update_score()

            if len(self.setting.find_valid_moves(self.current_player)) == 0:
                messagebox.showinfo('Attention please!', 'The game has to swap player.')
                print('swap player')
                self.clear_hint()
                self.current_player = 3 - self.current_player
                self.hinter()

class hard_black_bot(Blackbotboard):
    def __init__(self, master):
        super().__init__(master)

    def blackbot_play(self):
        valid_moves = self.setting.find_valid_moves(self.current_player)
        corner_moves = [(0, 0),(0, 1),(0, 2),(0, 3),(0, 4),(0, 5),(0, 6),(0, 7),
                        (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7), 
                        (7, 0),(7,1),(7,2),(7,3),(7,4),(7,5),(7,6), (7, 7)]
        middle_moves = [(2,2),(2,3),(2,4),(2,5),
                           (3,2),(3,3),(3,4),(3,5),
                           (4,2),(4,3),(4.4),(4.5),
                           (5,2),(5,3),(5,4),(5,5)]
        i, j = None, None  # Initialize i and j
        # Check if any corner move is a valid move and prioritize it
        for m in middle_moves:
             if m in valid_moves:
                  i,j = m
                  break
        for move in corner_moves:
            if move in valid_moves:
                i, j = move
                break

        if i is None:  # If no valid corner move, find any valid move
            if valid_moves:
                i, j = random.choice(valid_moves)

        if i is not None:
            self.setting.place_piece(i, j, self.current_player)
            self.clear_hint()
            self.current_player = 3 - self.current_player
            self.update_board()
            self.hinter()
            self.fixed_show_player()
            self.update_score()

            if len(self.setting.find_valid_moves(self.current_player)) == 0:
                messagebox.showinfo('Attention please!', 'The game has to swap player.')
                print('swap player')
                self.clear_hint()
                self.current_player = 3 - self.current_player
                self.hinter()
