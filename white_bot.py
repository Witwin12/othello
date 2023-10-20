from board import Board
import random

class white_bot(Board):
    def __init__(self, master):
        super().__init__(master)
        self.white_bot_play()
        
    def white_bot_play(self):
        if self.current_player == 2:
            valid_moves = self.setting.find_valid_moves(self.current_player)
            corner_moves = [(0, 0),(0, 1),(0, 2),(0, 3),(0, 4),(0, 5),(0, 6),(0, 7), (7, 0),(7,1),(7,2),(7,3),(7,4),(7,5),(7,6), (7, 7)]
        
            # Check if any corner move is a valid move and prioritize it
            for move in corner_moves:
                if move in valid_moves:
                    i, j = move
                    break
            else:
                # If no corner moves are valid, select a random valid move
                i, j = random.choice(valid_moves)
        
            print(f'Go GO {i},{j}')
            self.setting.place_piece(i, j, self.current_player)
            self.clear_hint()
            self.current_player = 3 - self.current_player
            self.update_board()
            self.hinter()
            self.fixed_show_player()
            self.update_score()


    def send(self, i, j):
        super().send(i, j)
        if self.current_player == 2:
            self.white_bot_play()
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
            self.white_bot_play()
