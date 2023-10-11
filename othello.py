# Import Tkinter module
import tkinter as tk

# Define constants for colors and cell size
black = 'b'
white = 'w'
void = '.'
cell_size = 50
colors = {black: 'black', white: 'white', void: 'grey'}
directions = [(-1,0),(1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
# Create a root window
root = tk.Tk()
root.title("Othello")

# Define a class that inherits from tk.Frame
class Board(tk.Frame):
    # Initialize the frame and its widgets
    def __init__(self, master):
        # Call the __init__ method of the tk.Frame class
        tk.Frame.__init__(self, master)
        # Create a canvas widget to draw the board on
        self.canvas = tk.Canvas(self, width=cell_size*8, height=cell_size*8)
        self.canvas.pack()
        # Bind the click function to the mouse click event on the canvas
        self.canvas.bind("<Button-1>", self.click)
        # Create a board list
        self.board = [[void]*8 for _ in range(8)]
        # Initialize the board with some values
        self.board[3][3] = white
        self.board[3][4] = black
        self.board[4][3] = black
        self.board[4][4] = white
        # Draw the initial board
        self.draw_board()
        self.color = black

    # Define a function to draw the board on the canvas
    def draw_board(self):
        # Draw the grid lines
        for i in range(9):
            self.canvas.create_line(i*cell_size, 0, i*cell_size, cell_size*8)
            self.canvas.create_line(0, i*cell_size, cell_size*8, i*cell_size)
        # Draw the cells
        for i in range(8):
            for j in range(8):
                color = colors[self.board[i][j]]
                self.canvas.create_rectangle(j*cell_size+1, i*cell_size+1, (j+1)*cell_size-1, (i+1)*cell_size-1, fill=color)
    def opposite(self):
        if self.color == black:
            return white
        elif self.color == white:
            return black
        else:
            return None
    # Define a function to handle mouse clicks on the canvas
    def click(self, event):
        # Get the row and column of the clicked cell
        row = event.y // cell_size
        col = event.x // cell_size
        valid = False
        if self.board[row][col] != void:
            return valid

        for dr,dc in directions:
            r = row+dr
            c = col+dc
            while 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] == self.opposite():
                r +=dr
                c += dc
                if 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] == self.color:
                    self.board[row][col] = self.color# update the board value
                    self.color = self.opposite()
                    valid = True
                    break
            if valid:
                # Move back to the original position
                r -= dr
                c -= dc
                # Flip the tiles until reaching the placed tile
                while r != row or c != col:
                    self.board[r][c] = self.color# flip the tile color
                    r -= dr
                    c -= dc
            return valid
        # Redraw the board
        self.draw_board()

        # Check for win or tie conditions (you can change this according to your game rules)
        self.check_result()

    # Define a function to check for win or tie conditions and display the result
    def check_result(self):
        # Count the number of black and white cells on the board
        black_count = 0
        white_count = 0
        for row in self.board:
            for cell in row:
                if cell == black:
                    black_count += 1
                elif cell == white:
                    white_count += 1

        # Display the result on the title bar of the root window
        if black_count + white_count == 64: # The board is full
            if black_count > white_count: # Black has more cells than white
                root.title("Black wins!")
            elif black_count < white_count: # White has more cells than black
                root.title("White wins!")
            else: # Black and white have equal number of cells
                root.title("It's a tie!")
        else: # The board is not full yet
            root.title(f"Black: {black_count}, White: {white_count}")
# Create an instance of the Board class and add it to the root window
board = Board(root)
board.pack()

# Run the main loop of the root window
root.mainloop()