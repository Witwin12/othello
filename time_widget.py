import tkinter as tk

class Time_widget(tk.Label):
    def __init__(self, master):
        super().__init__(master, text='Time: [0:00:00]', bg='light gray', font=('Grandview', 12))

        self.flag = True  # Set the flag to True
        self.timeSec = 0
        self.timeMin = 0
        self.timeHour = 0
        self.update_time()

    def update_time(self):
        if self.flag:
            self.timeSec += 1
            if self.timeSec == 60:
                self.timeSec = 0
                self.timeMin += 1
                if self.timeMin == 60:
                    self.timeMin = 0
                    self.timeHour += 1

            time_str = f'Time: [{self.timeHour:02d}:{self.timeMin:02d}:{self.timeSec:02d}]'
            self.configure(text=time_str)
            self.after(1000, self.update_time)
        else:
            self.configure(text=f'Time: [{self.timeHour:02d}:{self.timeMin:02d}:{self.timeSec:02d}]')

    def reset_time(self):
        self.timeSec = 0
        self.timeMin = 0
        self.timeHour = 0
        self.configure(text='Time: [00:00:00]')