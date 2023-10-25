from board import Board
from tkinter import messagebox
class easy_white_bot(Board):
    def __init__(self, master):
        super().__init__(master)
        
    def white_bot_play(self):
        if self.current_player == 2:#check a white turn
            valid_moves = self.setting.find_valid_moves(self.current_player)
            i,j = valid_moves[0]
            print(f'Go GO {i},{j}')
            self.setting.place_piece(i, j, self.current_player)
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
        if self.current_player == 2:
            self.white_bot_play()
            self.show_win()
class normal_white_bot(easy_white_bot):
    def __init__(self,master):
        super().__init__(master)
    def white_bot_play(self):
        if self.current_player == 2:#check a white turn
            valid_moves = self.setting.find_valid_moves(self.current_player)
            corner_moves = [(0, 0),(0, 1),(0, 2),(0, 3),(0, 4),(0, 5),(0, 6),(0, 7),
                            (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7), 
                            (7, 0),(7,1),(7,2),(7,3),(7,4),(7,5),(7,6), (7, 7)]
        
            # Check if any corner move is a valid move and prioritize it
            for move in corner_moves:
                if move in valid_moves:
                    i, j = move
                    break
                else:
                    #pick a first move 
                    i,j = valid_moves[0]
        
            print(f'Go GO {i},{j}')
            self.setting.place_piece(i, j, self.current_player)
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
class hard_white_bot(easy_white_bot):
    def __init__(self,master):
        super().__init__(master)
    def white_bot_play(self):
        if self.current_player == 2:#check a white turn
            valid_moves = self.setting.find_valid_moves(self.current_player)
            corner_moves = [(0, 0),(0, 1),(0, 2),(0, 3),(0, 4),(0, 5),(0, 6),(0, 7),
                        (1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7), 
                        (7, 0),(7,1),(7,2),(7,3),(7,4),(7,5),(7,6),(7, 7)]
            middle_moves = [(2,2),(2,3),(2,4),(2,5),
                           (3,2),(3,3),(3,4),(3,5),
                           (4,2),(4,3),(4.4),(4.5),
                           (5,2),(5,3),(5,4),(5,5)]
            # Check if any corner move is a valid move and prioritize it
            for m in middle_moves:
                 if m in valid_moves:
                      i,j = m
                      break
            else:
                for move in corner_moves:
                    if move in valid_moves:
                        i, j = move
                        break
                    else:
                        #pick a first move 
                        i,j = valid_moves[0]
            print(f'Go GO {i},{j}')
            self.setting.place_piece(i, j, self.current_player)
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
    