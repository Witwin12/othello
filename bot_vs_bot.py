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
            for m in middle_moves:# find middle move first
                 if m in valid_moves:
                      i,j = m
                      break
            else:
                for move in corner_moves: #find the corner move
                    if move in valid_moves:
                        i, j = move
                        break
                    else:
                        #pick a first move and last move
                        new_current_player = [valid_moves[0],valid_moves[-1]]
                        i, j = random.choice(new_current_player)
        
        self.setting.place_piece(i,j,self.current_player)
        self.current_player = 3 - self.current_player
        self.update_board()
        self.fixed_show_player()
        self.update_score()

        if len(self.setting.find_valid_moves(self.current_player)) == 0:
                print('swap player')
                self.current_player = 3 - self.current_player