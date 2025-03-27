"""
A bot that playes double XO
Author: Simi
"""

from player import Player
from full_board import FullBoard, copy_board
from const import EMPTY, PLAYER_X, PLAYER_O

DEFAULT_DEEPNESS = 3

class SimiBot(Player):
    def __init__(self, turn: int) -> None:
        super().__init__(turn)
    
    def play_turn(self, board: FullBoard):
        print("Calculating....")
        possible_moves = [None, None, None, None, None, None, None, None, None]
        for i in range(9):
            board_copy = copy_board(board)
            if self.play_move(board_copy, i, self.turn):
                possible_moves[i] = self.calculate_turn_status(
                    board_copy,
                    self.opposite_turn(self.turn)
                )
        print(possible_moves)
        index = self.pick_move(possible_moves)
        self.play_move(board, index, self.turn)
       
    def play_move(self, board: FullBoard, move_index: int, turn: int) -> bool:
        row = move_index // 3
        collumn = move_index % 3
        return board.place_on_current_board(row, collumn, turn)

    def pick_move(self, possible_moves: list) -> int:
        try:
            return possible_moves.index(self.turn)
        except ValueError:
            pass

        try:
            return possible_moves.index(EMPTY)
        except ValueError:
            pass

        for i in range(9):
            if not possible_moves[i] == None:
                return i
        
        return 0

    def calculate_turn_status(self, board: FullBoard, turn: int, deepness: int = DEFAULT_DEEPNESS) -> int:
        if board.check_win():
            return self.opposite_turn(turn)
        if deepness == 0:
            return EMPTY
        possible_moves = [None, None, None, None, None, None, None, None, None]
        for i in range(9):
            board_copy = copy_board(board)
            if self.play_move(board_copy, i, turn):
                possible_moves[i] = self.calculate_turn_status(
                    board_copy,
                    self.opposite_turn(turn),
                    deepness - 1
                )
        return possible_moves[self.pick_move(possible_moves)]

    @staticmethod
    def opposite_turn(turn):
        if turn == PLAYER_X:
            return PLAYER_O
        else:
            return PLAYER_X
