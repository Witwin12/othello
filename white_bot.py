from board import Board
import random
class white_bot(Board):
        
    def white_bot_play(self):
        if self.current_player == 2:#check a white turn
            valid_moves = self.setting.find_valid_moves(self.current_player)
            i,j = valid_moves[0]
            print(f'go go {i},{j}')
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

    