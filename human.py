from full_board import FullBoard
from player import Player
from const import EMPTY

class Human(Player):
    def __init__(self, turn: int):
        super().__init__(turn)
    
    def play_turn(self, board: FullBoard):
        if not board.get_current_board().won == EMPTY:
            #choose a board to play on, and set it as current board
            successfully_chose = False
            while not successfully_chose:
                row_str = input("Enter the board row you want to play in:\n")
                while not row_str.isdigit() or int(row_str) > 2 or int(row_str) < 0:
                    row_str = input("Invalid input! Try agian:\n")
            
                collumn_str = input("Enter the board collumn you want to play in:\n")
                while not collumn_str.isdigit() or int(collumn_str) > 2 or int(collumn_str) < 0:
                    collumn_str = input("Invalid input! Try agian:\n")
            
                successfully_chose = board.change_current_board(
                    int(row_str),
                    int(collumn_str)
                )
        #play on the current board
        successfully_placed = False
        while not successfully_placed:
            row_str = input("Enter the row you want to play in:\n")
            while not row_str.isdigit() or int(row_str) > 2 or int(row_str) < 0:
                row_str = input("Invalid input! Try agian:\n")
            
            collumn_str = input("Enter the collumn you want to play in:\n")
            while not collumn_str.isdigit() or int(collumn_str) > 2 or int(collumn_str) < 0:
                collumn_str = input("Invalid input! Try agian:\n")
            
            successfully_placed = board.place_on_current_board(
                int(row_str),
                int(collumn_str),
                self.turn
            )
