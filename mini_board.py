from const import Tile

class MiniBoard:
    def __init__(self) -> None:
        self.board = [
            [Tile.EMPTY, Tile.EMPTY, Tile.EMPTY],
            [Tile.EMPTY, Tile.EMPTY, Tile.EMPTY],
            [Tile.EMPTY, Tile.EMPTY, Tile.EMPTY]
        ]
        self.won = Tile.EMPTY
    
    def __repr__(self) -> str:
        match self.won:
            case Tile.EMPTY:
                return f""" _____ 
|{Tile.num_to_char(self.board[0][0])}|{Tile.num_to_char(self.board[0][1])}|{Tile.num_to_char(self.board[0][2])}|
|{Tile.num_to_char(self.board[1][0])}|{Tile.num_to_char(self.board[1][1])}|{Tile.num_to_char(self.board[1][2])}|
|{Tile.num_to_char(self.board[2][0])}|{Tile.num_to_char(self.board[2][1])}|{Tile.num_to_char(self.board[2][2])}|
 ‾‾‾‾‾ """
            case Tile.PLAYER_X:
                return f""" _____ 
|\\   /|
|  |  |
|/   \\|
 ‾‾‾‾‾ """
            case Tile.PLAYER_O:
                return f""" _____ 
| --- |
||   ||
| --- |
 ‾‾‾‾‾ """

    def place(self, row: int, collumn: int, turn: int) -> bool:
        #input check
        if row < 0 or row > 2:
            raise ValueError("row value must be between 0-2")
        elif collumn < 0 or collumn > 2:
            raise ValueError("collumn value must be between 0-2")
        elif not turn == Tile.PLAYER_X and not turn == Tile.PLAYER_O:
            raise ValueError(f"Turn value must be either {Tile.PLAYER_X} or {Tile.PLAYER_O}")
        
        if self.board[row][collumn] == Tile.PLAYER_X or self.board[row][collumn] == Tile.PLAYER_O:
            return False
        else:
            self.board[row][collumn] = turn
    
    def check_win(self) -> bool:
        """
        This function checks if someone has won,
        updates the 'won' value
        and returns True or False if someone has won
        """
        #check for 3 in a row
        for row in range(3):
            if (not self.board[row][0] == Tile.EMPTY
                and self.board[row][0] == self.board[row][1]
                and self.board[row][0] == self.board[row][2]):
                self.won = self.board[row][0]
                return True
        #check for 3 in a collumn
        for collumn in range(3):
            if (not self.board[0][collumn] == Tile.EMPTY
                and self.board[0][collumn] == self.board[1][collumn]
                and self.board[0][collumn] == self.board[2][collumn]):
                self.won = self.board[0][collumn]
                return True
        #check for 3 in a diagonal
        if (not self.board[0][0] == Tile.EMPTY
            and self.board[0][0] == self.board[1][1]
            and self.board[0][0] == self.board[2][2]):
            self.won = self.board[0][0]
            return True
        if (not self.board[0][2] == Tile.EMPTY
            and self.board[0][2] == self.board[1][1]
            and self.board[0][2] == self.board[2][0]):
            self.won = self.board[0][2]
            return True
        self.won = Tile.EMPTY
        return False
