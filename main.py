from player import Player
from human import Human
from simi_bot import SimiBot
from full_board import FullBoard
from const import Tile
from time import sleep

def game(playerX: Player, playerO: Player, board: FullBoard):
    turn = True
    while not board.check_win():
        print(board)
        if turn:
            print("It's player X's turn!")
            playerX.play_turn(board)
        else:
            print("It's player O's turn!")
            playerO.play_turn(board)
        turn = not turn
    print(board)
    if turn:
        print("Player X won!")
    else:
        print("Player O won!")
    sleep(3)

def main():
    player1 = Human(Tile.PLAYER_X)
    player2 = SimiBot(Tile.PLAYER_O)
    board = FullBoard()
    game(player1, player2, board)

if __name__ == "__main__":
    main()