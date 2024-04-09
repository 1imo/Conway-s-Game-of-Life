# Individual cell
class Cell:
    # State of the cell (dead or alive)
    # Default state is dead
    state: bool = False

    # Cell value when printed
    def __str__(self) -> str:
        if self.state:
            return "O"
        else:
            return "."

    # Get the state of the cell
    def get_state(self) -> bool:
        return self.state

    # Invert the state of the cell
    def change_state(self) -> None:
        self.state = not self.state

    # Set the state of the cell
    def set_state(self, state: bool) -> None:
        self.state = state
