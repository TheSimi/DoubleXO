from abc import ABC
from full_board import FullBoard
from const import Tile

class Player(ABC):
    def __init__(self, turn: int):
        if not turn == Tile.PLAYER_X and not turn == Tile.PLAYER_O:
            raise ValueError(f"turn must be either {Tile.PLAYER_X} or {Tile.PLAYER_O}")
        
        self.turn = turn
    
    def play_turn(self, board: FullBoard) -> bool:
        """
        plays a turn in the game
        returns True if this player won the game or False otherwise
        """
        pass