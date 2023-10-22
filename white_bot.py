from board import Board
import random
class easy_white_bot(Board):
    def __init__(self, master):
        super().__init__(master)
        
    def white_bot_play(self):
        if self.current_player == 2:#check a white turn
            valid_moves = self.setting.find_valid_moves(self.current_player)
            i,j = random.choice(valid_moves)
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
                new_current_player = [valid_moves[0],valid_moves[-1]]
                i, j = random.choice(new_current_player)
        
            print(f'Go GO {i},{j}')
            self.setting.place_piece(i, j, self.current_player)
            self.clear_hint()
            self.current_player = 3 - self.current_player
            self.update_board()
            self.hinter()
            self.fixed_show_player()
            self.update_score()
class hard_white_bot(easy_white_bot):
    def __init__(self,master):
        super().__init__(master)