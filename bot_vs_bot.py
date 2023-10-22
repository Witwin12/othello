from board import Board
import random

class Botvsbot(Board):
    def __init__(self, master):
        super().__init__(master)
        self.gamestate = False
        self.auto()
        

    def send(self, i, j):
        pass

    def auto(self):
        self.clear_hint()
        if self.gamestate:
            if self.current_player == 1:
                self.blackbot_play()
            else:
                self.whitebot_play()
            
            if len(self.setting.find_valid_moves(1)) ==0 and len(self.setting.find_valid_moves(2))==0:
                 self.show_win()
        self.after(1000, self.auto)

    def blackbot_play(self):
        i,j = random.choice(self.setting.find_valid_moves(self.current_player))
        self.setting.place_piece(i,j,self.current_player)
        self.current_player = 3 - self.current_player
        self.update_board()
        self.fixed_show_player()
        self.update_score()

        if len(self.setting.find_valid_moves(self.current_player)) == 0:
                print('swap player')
                self.current_player = 3 - self.current_player

    
    def whitebot_play(self):
        i,j = random.choice(self.setting.find_valid_moves(self.current_player))
        self.setting.place_piece(i,j,self.current_player)
        self.current_player = 3 - self.current_player
        self.update_board()
        self.fixed_show_player()
        self.update_score()

        if len(self.setting.find_valid_moves(self.current_player)) == 0:
                print('swap player')
                self.current_player = 3 - self.current_player