from const import EMPTY, PLAYER_X, PLAYER_O

class MiniBoard:
    def __init__(self) -> None:
        self.board = [
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]
        ]
        self.won = EMPTY
    
    def __repr__(self) -> str:
        match self.won:
            case int(EMPTY):
                return f""" _____ 
|{self.num_to_char(self.board[0][0])}|{self.num_to_char(self.board[0][1])}|{self.num_to_char(self.board[0][2])}|
|{self.num_to_char(self.board[1][0])}|{self.num_to_char(self.board[1][1])}|{self.num_to_char(self.board[1][2])}|
|{self.num_to_char(self.board[2][0])}|{self.num_to_char(self.board[2][1])}|{self.num_to_char(self.board[2][2])}|
 ‾‾‾‾‾ """
            case int(PLAYER_X):
                return f""" _____ 
|\\   /|
|  |  |
|/   \\|
 ‾‾‾‾‾ """
            case int(PLAYER_O):
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
        elif not turn == PLAYER_X and not turn == PLAYER_O:
            raise ValueError(f"Turn value must be either {PLAYER_X} or {PLAYER_O}")
        
        if self.board[row][collumn] == PLAYER_X or self.board[row][collumn] == PLAYER_O:
            return False
        else:
            self.board[row][collumn] = turn
            return True
    
    def check_win(self) -> bool:
        """
        This function checks if someone has won,
        updates the 'won' value
        and returns True or False if someone has won
        """
        #check for 3 in a row
        for row in range(3):
            if (not self.board[row][0] == EMPTY
                and self.board[row][0] == self.board[row][1]
                and self.board[row][0] == self.board[row][2]):
                self.won = self.board[row][0]
                return True
        #check for 3 in a collumn
        for collumn in range(3):
            if (not self.board[0][collumn] == EMPTY
                and self.board[0][collumn] == self.board[1][collumn]
                and self.board[0][collumn] == self.board[2][collumn]):
                self.won = self.board[0][collumn]
                return True
        #check for 3 in a diagonal
        if (not self.board[0][0] == EMPTY
            and self.board[0][0] == self.board[1][1]
            and self.board[0][0] == self.board[2][2]):
            self.won = self.board[0][0]
            return True
        if (not self.board[0][2] == EMPTY
            and self.board[0][2] == self.board[1][1]
            and self.board[0][2] == self.board[2][0]):
            self.won = self.board[0][2]
            return True
        self.won = EMPTY
        return False
    
    @staticmethod
    def num_to_char(num: int):
        match num:
            case int(EMPTY):
                return '-'
            case int(PLAYER_X):
                return 'X'
            case int(PLAYER_O):
                return 'O'
            case _:
                raise ValueError(f"A tile value must be one of these: \
                    {EMPTY}, {PLAYER_X}, {PLAYER_O}")

def copy_mini_board(original_mini_board: MiniBoard) -> MiniBoard:
    new_mini_board = MiniBoard()
    for i in range(3):
        for j in range(3):
            new_mini_board.board[i][j] = original_mini_board.board[i][j]
    new_mini_board.won = original_mini_board.won
    return new_mini_board
