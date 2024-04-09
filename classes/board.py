from classes.cell import Cell


# Board class
class Board:
    board: list[list[Cell]]
    board_size: int

    # Constructor
    # Initializes the board as a 2D array with the given size
    def __init__(self, size: int) -> None:
        self.board = [[Cell() for _ in range(size)] for _ in range(size)]
        self.board_size = size

    # Board value when printed
    def __str__(self) -> str:
        return "\n".join([" ".join([str(cell) for cell in row]) for row in self.board])

    # Set the state of a cell at the given coordinates
    # X, Y: Coordinates of the cell on the board
    # If the value is None, the state of the cell is toggled
    def set_item(self, x, y, value) -> None:
        if value is None:
            self.board[self.board_size - y - 1][x].change_state()
        else:
            self.board[self.board_size - y - 1][x].set_state(value)

    # Sliding window to count the number of live neighbors of a cell
    # X, Y: Coordinates of the cell on the board
    # Returns the number of live neighbors
    def count_live_neighbors(self, x, y):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                nx = x + i
                ny = y + j
                if (
                    0 <= nx < self.board_size
                    and 0 <= ny < self.board_size
                    and self.board[nx][ny].get_state()
                ):
                    count += 1
        return count

    # Iterator for the board
    def __iter__(self):
        return iter(self.board)

    def __getitem__(self, index):
        return self.board[index]
