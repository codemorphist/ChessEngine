from ChessEngine.pieces import Piece
from ChessEngine.utils import Coord
from ChessEngine.utils.checkers import *


class Knight(Piece):
    """
    Class of Knight
    """

    def get_moves(self, pos: Coord, board):
        """
        Return all moves from current position
        """
        x, y = pos
        for i, j in [(1, 2), (1, -2), (-1, 2), (-1, -2),
                     (2, 1), (-2, 1), (2, -1), (-2, -1)]:
            if can_move(Coord(x+i, y+j), board):
                yield Coord(x+i, y+j)

    def get_attack(self, pos: Coord, board):
        """
        Return all attack moves from current position
        """
        x, y = pos
        for i, j in [(1, 2), (1, -2), (-1, 2), (-1, -2),
                     (2, 1), (-2, 1), (2, -1), (-2, -1)]:
            if can_attack(self, Coord(x+i, y+j), board):
                yield Coord(x+i, y+j)
