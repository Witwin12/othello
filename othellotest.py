# Othello game in python

# Define the constants
BOARD_SIZE = 8
BLACK = "B"
WHITE = "W"
EMPTY = "."

# Define the directions
UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
UP_LEFT = (-1, -1)
UP_RIGHT = (-1, 1)
DOWN_LEFT = (1, -1)
DOWN_RIGHT = (1, 1)

# Define the list of all directions
DIRECTIONS = [UP, DOWN, LEFT, RIGHT, UP_LEFT, UP_RIGHT, DOWN_LEFT, DOWN_RIGHT]

# Define the opposite color function
def opposite(color):
    if color == BLACK:
        return WHITE
    elif color == WHITE:
        return BLACK
    else:
        return None

# Define the create board function
def create_board():
    # Create an empty board
    board = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    # Place the initial four tiles in the center
    half = BOARD_SIZE // 2
    board[half - 1][half - 1] = WHITE
    board[half][half] = WHITE
    board[half - 1][half] = BLACK
    board[half][half - 1] = BLACK
    # Return the board
    return board

# Define the print board function
def print_board(board):
    # Print the column numbers
    print(" ", end=" ")
    for i in range(BOARD_SIZE):
        print(i, end=" ")
    print()
    # Print the rows with numbers
    for i in range(BOARD_SIZE):
        print(i, end=" ")
        for j in range(BOARD_SIZE):
            print(board[i][j], end=" ")
        print()
    print()

# Define the is valid move function
def is_valid_move(board, color, row, col):
    # Check if the position is empty
    if board[row][col] != EMPTY:
        return False
    # Check if the position is on the board
    if not (0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE):
        return False
    # Check if the move can flip any tile in any direction
    for dr, dc in DIRECTIONS:
        # Start from the adjacent position
        r = row + dr
        c = col + dc
        # Keep moving in that direction until reaching a valid tile or the edge of the board
        while 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and board[r][c] == opposite(color):
            r += dr
            c += dc
            # If a tile of the same color is found, then the move is valid
            if 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and board[r][c] == color:
                return True
    # If no direction can flip any tile, then the move is invalid
    return False

# Define the get valid moves function
def get_valid_moves(board, color):
    # Create an empty list of valid moves
    valid_moves = []
    # Loop through all positions on the board
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            # If the position is a valid move, add it to the list
            if is_valid_move(board, color, i, j):
                valid_moves.append((i, j))
    # Return the list of valid moves
    return valid_moves

# Define the make move function
def make_move(board, color, row, col):
    # Place the tile on the board
    board[row][col] = color
    # Flip any tile in any direction that can be flipped by this move
    for dr, dc in DIRECTIONS:
        # Start from the adjacent position
        r = row + dr
        c = col + dc
        # Keep moving in that direction until reaching a valid tile or the edge of the board
        while 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and board[r][c] == opposite(color):
            r += dr
            c += dc
            # If a tile of the same color is found, flip all the tiles in between
            if 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and board[r][c] == color:
                # Move back to the original position
                r -= dr
                c -= dc
                # Flip the tiles until reaching the placed tile
                while r != row or c != col:
                    board[r][c] = color
                    r -= dr
                    c -= dc

# Define the get score function
def get_score(board, color):
    # Initialize the score to zero
    score = 0
    # Loop through all positions on the board
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            # If the position has a tile of the given color, increase the score by one
            if board[i][j] == color:
                score += 1
    # Return the score
    return score

# Define the main function
def main():
    # Create the board
    board = create_board()
    # Print the board
    print_board(board)
    # Set the initial color to black
    color = BLACK
    # Set the game over flag to false
    game_over = False
    # Start the game loop
    while not game_over:
        # Get the valid moves for the current color
        valid_moves = get_valid_moves(board, color)
        # If there are no valid moves, skip the turn
        if not valid_moves:
            print(color, "has no valid moves. Skipping...")
            # Switch the color
            color = opposite(color)
            # Check if the game is over
            if not get_valid_moves(board, color):
                game_over = True
            continue
        # Print the valid moves for the current color
        print(color, "has", len(valid_moves), "valid moves:", valid_moves)
        # Get the user input for the move
        row, col = map(int, input("Enter row and column for " + color + ": ").split())
        # Validate the user input
        while (row, col) not in valid_moves:
            print("Invalid move. Try again.")
            row, col = map(int, input("Enter row and column for " + color + ": ").split())
        # Make the move on the board
        make_move(board, color, row, col)
        # Print the board
        print_board(board)
        # Switch the color
        color = opposite(color)
        # Check if the game is over
        if not get_valid_moves(board, color):
            game_over = True

    # Print the final scores and the winner
    black_score = get_score(board, BLACK)
    white_score = get_score(board, WHITE)
    print("Game over!")
    print("Black:", black_score)
    print("White:", white_score)
    if black_score > white_score:
        print("Black wins!")
    elif white_score > black_score:
        print("White wins!")
    else:
        print("It's a tie!")

# Run the main function
if __name__ == "__main__":
    main()
