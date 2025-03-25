from mini_board import MiniBoard

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

    def place(self, row: int, collumn: int, turn: int) -> bool:
        if self.get_current().place(row, collumn, turn):
            self.current_row = row
            self.current_collumn = collumn
            return True
        return False