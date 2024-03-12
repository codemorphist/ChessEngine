from ChessEngine.pieces import Piece
from ChessEngine.utils import Coord
from ChessEngine.utils.checkers import *


class Pawn(Piece):
    """
    Class of Pawn
    """

    def get_moves(self, pos: Coord, board):
        """
        Return all moves from current position
        """
        x, y = pos
        i = 1 if self.color is Color.Black else -1
        if can_move(Coord(x, y + i), board):
            yield Coord(x, y + i)

            if y in [1, 6] and can_move(Coord(x, y + 2 * i), board):
                yield Coord(x, y + i + i)

    def get_attack(self, pos: Coord, board):
        """
        Return all attack moves from current position
        """
        x, y = pos
        for pattern in [(-1, -1), (1, -1)]:
            i, j = pattern
            if self.color is Color.Black:
                i, j = -i, -j
            if can_attack(self, Coord(x + i, y + j), board):
                yield Coord(x + i, y + j)
