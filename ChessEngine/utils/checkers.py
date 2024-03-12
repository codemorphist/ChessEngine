from ChessEngine.pieces import *
from ChessEngine.utils import Coord
from ChessEngine.utils.enums import Color


def on_board(pos: Coord) -> bool:
    x, y = pos
    return 0 <= x <= 7 and 0 <= y <= 7




def can_attack(fig: Piece, pos: Coord, board: list[list[Piece]]) -> bool:
    x, y = pos
    if not on_board(pos):
        return False
    attacked = board[y][x]
    return attacked is not None and attacked.color is not fig.color


def can_move(pos: Coord, board: list[list[Piece]]) -> bool:
    x, y = pos
    return on_board(pos) and board[y][x] is None
