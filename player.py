from abc import ABC
from full_board import FullBoard
from const import PLAYER_X, PLAYER_O

class Player(ABC):
    def __init__(self, turn: int):
        if not turn == PLAYER_X and not turn == PLAYER_O:
            raise ValueError(f"turn must be either {PLAYER_X} or {PLAYER_O}")
        
        self.turn = turn
    
    def play_turn(self, board: FullBoard) -> bool:
        """
        plays a turn in the game
        returns True if this player won the game or False otherwise
        """
        pass