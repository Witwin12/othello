import tkinter as tk
from setting import Setting
print(Setting.time)
class Counttime:
    def __init__(self, root):
        self.root = root
        self.root.title('Count-Up Timer')
        
        self.elapsed_time = 0
        self.timer_label = tk.Label(root, text="Elapsed time: 0 seconds", font=("Arial", 16))
        self.timer_label.place(x=700,y=300)
        self.update_timer()
    def update_timer(self):
        if Setting.time == 0:
            self.elapsed_time += 1
            self.timer_label.config(text=f"Elapsed time: {self.elapsed_time} seconds")
            self.root.after(1000, self.update_timer)  # Schedule the update after 1000 ms (1 second)
        else:
            self.timer_label.config(text=f"Elapsed time: {self.elapsed_time} seconds")
        print(Setting.time)



    
