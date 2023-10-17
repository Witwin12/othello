import tkinter as tk

class Time_widget(tk.Label):
    def __init__(self, master):
        super().__init__(master, text='Time: (0: 0)')

        self.flag  =True#สร้างธงให้เป็นจริง
        self.timeMin = 0
        self.timeSec = 0
        self.update_time()

    def update_time(self):
        if self.flag :
            self.timeSec += 1
            if  self.timeSec == 60:
                self.timeSec = 0
                self.timeMin += 1
            self.configure(text=f'Time: ({self.timeMin}:{self.timeSec})')
            self.after(1000, self.update_time)  # ตั้งเวลาเรียกใหม่ทุกวินาที
        else:#๔้าธงเป็น้ท็จให้หยุดเวลา
            self.configure(text=f'Time: ({self.timeMin}:{self.timeSec})')

    def reset_time(self):
        self.timeMin = 0
        self.timeSec = 0
        self.configure(text='Time: (0: 0)')
    
