"""
A bot that playes double XO
Author: Simi
"""

from player import Player
from full_board import FullBoard, copy_board
import const
import random

EMPTY = const.EMPTY
PLAYER_X = const.PLAYER_X
PLAYER_O = const.PLAYER_O

DEFAULT_DEEPNESS = const.DEFAULT_DEEPNESS

ILEAGAL_MOVES = const.ILEAGAL_MOVES
UNKNOWN_MOVES = const.UNKNOWN_MOVES
X_WINS_MOVES = const.X_WINS_MOVES
O_WINS_MOVES = const.O_WINS_MOVES

class SimiBot(Player):
    def __init__(self, turn: int) -> None:
        super().__init__(turn)
    
    def play_turn(self, board: FullBoard):
        print("Calculating best move...")
        move = self.find_best_move(board, self.turn, origin=True)
        self.play_move(board, move, self.turn)
       
    def play_move(self, board: FullBoard, move_index: int, turn: int) -> bool:
        row = move_index // 3
        collumn = move_index % 3
        return board.place_on_current_board(row, collumn, turn)

    def pick_move(self, possible_moves: list, turn: int) -> int:
        #if can force win
        if turn == PLAYER_X and len(possible_moves[X_WINS_MOVES]) > 0:
            return random.choice(possible_moves[X_WINS_MOVES])
        elif turn == PLAYER_O and len(possible_moves[O_WINS_MOVES]) > 0:
            return random.choice(possible_moves[O_WINS_MOVES])
        #if can avoid forced loss
        elif len(possible_moves[UNKNOWN_MOVES]) > 0:
            return random.choice(possible_moves[UNKNOWN_MOVES])
        #no choice...
        elif turn == PLAYER_X and len(possible_moves[O_WINS_MOVES]) > 0:
            return random.choice(possible_moves[O_WINS_MOVES])
        elif turn == PLAYER_O and len(possible_moves[X_WINS_MOVES]) > 0:
            return random.choice(possible_moves[X_WINS_MOVES])
        #wait, what?
        else:
            raise Exception("No legal move to play!")
    
    def pick_move_type(self, possible_moves: list, turn: int) -> int:
        if turn == PLAYER_X and len(possible_moves[X_WINS_MOVES]) > 0:
            return X_WINS_MOVES
        elif turn == PLAYER_O and len(possible_moves[O_WINS_MOVES]) > 0:
            return O_WINS_MOVES
        elif len(possible_moves[UNKNOWN_MOVES]) > 0:
            return UNKNOWN_MOVES
        else:
            raise Exception("No legal move to play!")    

    def find_best_move(self, board: FullBoard, turn: int, deepness: int = DEFAULT_DEEPNESS, origin: bool = False):
        if deepness == 0:
            return UNKNOWN_MOVES
        if board.get_current_board().check_win():
            if origin:
                possible_boards = [[], [], [], []]
                for i in range(9):
                    board_copy = copy_board(board)
                    board_status = ILEAGAL_MOVES
                    if board_copy.change_current_board(i // 3, i % 3):
                        board_status = self.find_best_move(board_copy, turn, deepness=deepness)
                    possible_boards[board_status].append(i)
                board_pick = self.pick_move(possible_boards, turn)
                board.change_current_board(board_pick // 3, board_pick % 3)
                print(f"Playing on board ({board_pick //3}, {board_pick % 3})")
                return self.find_best_move(board, turn, deepness=deepness, origin=True)
            else:
                possible_boards = [[], [], [], []]
                for i in range(9):
                    board_copy = copy_board(board)
                    board_status = ILEAGAL_MOVES
                    if board_copy.change_current_board(i // 3, i % 3):
                        board_status = self.find_best_move(board_copy, turn, deepness=deepness)
                    possible_boards[board_status].append(i)
                return self.pick_move_type(possible_boards, turn)
        else:
            #TODO - spliting into different functions
            possible_moves = [[], [], [], []]
            for i in range(9):
                board_copy = copy_board(board)
                move_status = ILEAGAL_MOVES
                if self.play_move(board_copy, i, turn):
                    if board_copy.check_win():
                        if turn == PLAYER_X:
                            move_status = X_WINS_MOVES
                        elif turn == PLAYER_O:
                            move_status = O_WINS_MOVES
                    else:
                        move_status = self.find_best_move(
                            board_copy,
                            self.opposite_turn(turn),
                            deepness=deepness - 1
                        )
                possible_moves[move_status].append(i)
            if origin:
                return self.pick_move(possible_moves, turn)
            else:
                return self.pick_move_type(possible_moves, turn)

    @staticmethod
    def opposite_turn(turn):
        if turn == PLAYER_X:
            return PLAYER_O
        else:
            return PLAYER_X
