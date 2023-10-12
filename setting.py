# สีดำ เป็น 1
# สีขาว เป็น 2
# วางได้ เป็น 3

class Setting():
    def __init__(self):     # 0  1  2  3  4  5  6  7 i เชี่ยนี่ แนวนอน
        self.table_matrix = [[0, 0, 0, 0, 0, 0, 0, 0],#0
                             [0, 0, 0, 0, 0, 0, 0, 0],#1
                             [0, 0, 0, 0, 0, 0, 0, 0],#2
                             [0, 0, 0, 2, 1, 0, 0, 0],#3
                             [0, 0, 0, 1, 2, 0, 0, 0],#4
                             [0, 0, 0, 0, 0, 0, 0, 0],#5
                             [0, 0, 0, 0, 0, 0, 0, 0],#6
                             [0, 0, 0, 0, 0, 0, 0, 0]]#7 ส่วนเชี่ยนี่ แนวตั้ง
        UP = (-1, 0)
        DOWN = (1, 0)
        LEFT = (0, -1)
        RIGHT = (0, 1)
        UP_LEFT = (-1, -1)# all directions
        UP_RIGHT = (-1, 1)
        DOWN_LEFT = (1, -1)
        DOWN_RIGHT = (1, 1)
        self.DIRECTIONS = [UP, DOWN, LEFT, RIGHT, UP_LEFT, UP_RIGHT, DOWN_LEFT, DOWN_RIGHT]                                                  
    def bpcheck(self): #(4,5)(5,4)(3,2),(2,3)
        for i in range(7):
            for j in range(7):
                if self.table_matrix[i][j] == 2 and 0 <= i <8 and 0<= j <8:# check index prevent index out of range
                    count = 0
                    for x,y in self.DIRECTIONS:
                        if self.table_matrix[i+x][j+y] ==0:
                            print(self.table_matrix[i+x][j+y])
                            print(f"position:{i+x,j+y}")# checK เฉยๆเขียนเสร๊จเดี๋ยวลบ
                            count +=1
                            print(f"total:{count}")
    def count(self):    
        score_black = 0
        score_white = 0
        for i in range(7):
            for j in range(7):
                if self.table_matrix[i][j] == 1 :
                    score_black +=1
                elif self.table_matrix[i][j] == 2:
                    score_white +=1  
a = Setting()
a.bpcheck()