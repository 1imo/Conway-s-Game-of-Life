from classes.board import Board
import time
import os

# Declaration of board size (user input)
board_size = int(input("Enter the size of the board: "))

# Current board instantiation
board = Board(board_size)

# Process initial board state from the seed file
with open("seed.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line:
            x, y = map(int, line.split())
            if 0 <= x < board_size and 0 <= y < board_size:
                board.set_item(x, y, True)

# Render the board in an indefinite loop
while True:
    # Next board state instantiation
    next_board = Board(board_size)

    # Update the state of each cell based on the rules of the game
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            # Count the number of live neighbors
            live_neighbors = board.count_live_neighbors(i, j)

            # If the cell is alive, check if it will survive or die
            # Else if the cell is dead, check if it will be born
            if cell.get_state():
                if live_neighbors < 2 or live_neighbors > 3:
                    next_board[i][j].set_state(False)  # Dies (Rule 1 and 3)
                else:
                    next_board[i][j].set_state(True)  # Lives (Rule 2)
            else:
                if live_neighbors == 3:  # Rule 4
                    next_board[i][j].set_state(True)  # Is born (Rule 4)
                else:
                    next_board[i][j].set_state(False)  # Stays dead

    # Update the original board with the next state
    board = next_board

    # Clear the terminal
    os.system("clear")

    # Print the updated board
    print(board)

    # Pause execution for 1 second
    time.sleep(1)
