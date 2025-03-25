class Tile:
    EMPTY = 0
    PLAYER_X = 1
    PLAYER_O = 2
    
    @staticmethod
    def num_to_char(num: int):
        match num:
            case Tile.EMPTY:
                return '-'
            case Tile.PLAYER_X:
                return 'X'
            case Tile.PLAYER_O:
                return 'O'
            case _:
                raise ValueError(f"A tile value must be one of these: \
                    {Tile.EMPTY}, {Tile.PLAYER_X}, {Tile.PLAYER_O}")