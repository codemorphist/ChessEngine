from ChessEngine.utils.enums import Color
from ChessEngine.utils import Coord


class Piece:
    def __init__(self, color: Color):
        """
        :param color: color of piece
        """
        self.color: Color = color

    def get_moves(self, pos: Coord, board):
        """
        Return all moves from current position
        """
        pass

    def get_attack(self, pos: Coord, board):
        """
        Return all attack moves from current position
        """
        pass
