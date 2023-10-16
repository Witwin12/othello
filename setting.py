# สีดำ เป็น 1
# สีขาว เป็น 2
#โมดูลนี้มีคลาส Setting ทำไว้ใส่กติกาของเกม Othello
class Setting():
    def __init__(self):
        # เป็นกระดานของเกมนี้ โดย (0 แทนจุดที่ไม่มีอะไรเลย) (1 แทนจุดที่มีหมากตวดำอยู่) (2 แทนจุดที่มีหมากตัวขาวอยู่)
        self.table_matrix = [[0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 2, 1, 0, 0, 0],
                             [0, 0, 0, 1, 2, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0]]

    def find_valid_moves(self, player):
        # methode นี้ใช้หาจุดที่ผู่เล่นวางได้โดยใส่ player ด้วยตัวเลข 1 หมายถึงผู้เล่นหมากดำ ตัวเลข 2 หมายถึงผู้เล่นหมากขาว และจะ return list ที่มีจุดที่วางได้อยู่
        # วิธีใช้งาน >>>> แค่ใส่เลข (1, 2) ผู้เล่นไป จะได้ list ของจุดที่วางได้มา
        valid_moves = []

        for i in range(8): # ตรวจทุกช่อง
            for j in range(8):
                if self.is_valid_move(i, j, player): # หาจุดที่วางได้
                    valid_moves.append((i, j)) # ใส่ในลิสต์

        return valid_moves 

    def is_valid_move(self, i, j, player):
        if self.table_matrix[i][j] != 0: #ตัดจุดที่ไม่ใช่ 0 ออก และ return ค่า False เพื่อบอกว่าตรงนั้นวางไม่ได้
            return False

        for x, y in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]: # การตรวจแบบขยับทุกแกน เช่น แถวที่(i, j) ด้านซ้ายของมันคือ (i-1, j)
            x_pos, y_pos = i + x, j + y
            if 0 <= x_pos < 8 and 0 <= y_pos < 8 and self.table_matrix[x_pos][y_pos] == 3 - player: # ถ้าเป็นหมากของอีกฝั่งหนึ่ง
                while 0 <= x_pos < 8 and 0 <= y_pos < 8 and self.table_matrix[x_pos][y_pos] == 3 - player: # ตราบใดที่ยังเป็นหมากอีกฝ่ายอยู่ให้ตรวจแบบขยับตามแกนนั้น
                    x_pos += x                                                                             # จนกว่าจะเป็นอย่างอื่น แต่ในที่นี้อาจจะมีหมากของฝ่ายเรา หรือไม่มีหมากก็ได้
                    y_pos += y

                if 0 <= x_pos < 8 and 0 <= y_pos < 8 and self.table_matrix[x_pos][y_pos] == player: # หาหมากของฝ่ายเราถ้าใช่ แสดงว่าจุดนั้นวางได้ จึง return True
                    return True

        return False # ถ้าไม่มีหมากก็จะ return False มาให้
    
    def place_piece(self, i, j, player):
        if self.is_valid_move(i, j, player):
            self.table_matrix[i][j] = player
            self.flip_pieces(i, j, player)

    def flip_pieces(self, i, j, player):
        # methode นี้ใช้เปลี่ยนตัวที่ถูกหนีบแล้ว ให้เป็นหมากของฝ่ายที่หนีบ โดย methode นี้บังคับใช้กับ methode place_piece เท่านั้น
        # วิธีใช้ >>>>>> ไม่ได้ออกแบบมาให้ใช้โดยตรง !!!!!!
        for x, y in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]: # ตรวจแบบขยับทุกแกน
            x_pos, y_pos = i + x, j + y
            if 0 <= x_pos < 8 and 0 <= y_pos < 8 and self.table_matrix[x_pos][y_pos] == 3 - player: # ตรวจแบบขยับตามแกน หาหมากอีกฝ่ายจนกว่าจะไม่เจอ
                temp = [] # list ว่างไว้เก็บช่องที่หมากอีกฝ่าย เพื่อที่จะเตรียมเปลี่ยน
                while 0 <= x_pos < 8 and 0 <= y_pos < 8 and self.table_matrix[x_pos][y_pos] == 3 - player:
                    temp.append((x_pos, y_pos))
                    x_pos += x
                    y_pos += y

                if 0 <= x_pos < 8 and 0 <= y_pos < 8 and self.table_matrix[x_pos][y_pos] == player: # หากเจอหมากฝ่ายเดียวกัน เปลี่ยนหมากอีกฝั่งได้เลย
                    for pos in temp:                                                                # ถ้าไม่ ไม่ทำอะไรเลย
                        self.table_matrix[pos[0]][pos[1]] = player

    def display_board(self): # ไว้โชว์สถานะกระดานแบบ UI ไว้ให้ผู้ใช้ดูความคืบหน้าของเกมได้
        for row in self.table_matrix:
            print(' '.join(map(str, row)))   # แปลงเป็น str แล้วมาต่อกันด้วยสตริงเว้นวรรค
    

    def determine_winner(self): # ใช้เมื่อเกมจบแล้ว หาผู้ชนะ แพ้ เสมอ
        player1_score = sum(row.count(1) for row in self.table_matrix)
        player2_score = sum(row.count(2) for row in self.table_matrix)

        if player1_score > player2_score:
            return "สีดำชนะ!"
        elif player2_score > player1_score:
            return "สีขาวชนะ!"
        else:
            return "เกมเสมอ!"                    