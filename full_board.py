from mini_board import MiniBoard
from const import Tile

class FullBoard:
    def __init__(self) -> None:
        self.board = [
            [MiniBoard(), MiniBoard(), MiniBoard()],
            [MiniBoard(), MiniBoard(), MiniBoard()],
            [MiniBoard(), MiniBoard(), MiniBoard()]
        ]
        self.current_row = 1
        self.current_collumn = 1

    def __repr__(self) -> str:
        final_str = ""
        for row in self.board:
            row_str = ["", "", "", "", ""]
            for mini_board in row:
                split_board = str(mini_board).split("\n")
                for i in range(len(split_board)):
                    row_str[i] += split_board[i]
                    row_str[i] += ' '
            for line in row_str:
                final_str += line
                final_str += '\n'
        final_str += f"current board is ({self.current_row}, {self.current_collumn}):\n"
        final_str += str(self.get_current())
        return final_str
    
    def get_current(self) -> MiniBoard:
        return self.board[self.current_row][self.current_collumn]
