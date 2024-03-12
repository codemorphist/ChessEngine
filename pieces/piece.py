from utils.enums import Color
from utils.utils import Coord


class Piece:
    def __init__(self, pos: Coord, color: Color):
        """
        :param pos: position on board of piece 
        :param color: color of piece 
        """
        self.pos: Coord = pos
        self.color: Color = color

    def move(self, dest: Coord):
        """
        Move figure to new position
        """
        self.pos = dest

    def get_moves(self, board):
        """
        Return all moves from current position
        """
        pass

    def get_attack(self, board):
        """
        Return all attack moves from current position
        """
        pass
