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
    
    def get_current_board(self) -> MiniBoard:
        return self.board[self.current_row][self.current_collumn]

    def place_on_current_board(self, row: int, collumn: int, turn: int) -> bool:
        if not self.get_current_board().won == Tile.EMPTY:
            return False
        if self.get_current_board().place(row, collumn, turn):
            self.current_row = row
            self.current_collumn = collumn
            return True
        return False
    
    def change_current_board(self, row: int, collumn: int) -> bool:
        if row < 0 or row > 2:
            raise ValueError("row value must be between 0-2")
        elif collumn < 0 or collumn > 2:
            raise ValueError("collumn value must be between 0-2")
        
        if not self.board[row][collumn].wom == Tile.EMPTY:
            return False
        else:
            self.current_row = row
            self.current_collumn = collumn
            return True
