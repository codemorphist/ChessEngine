from ChessEngine.pieces import Piece, Bishop, Rook
from ChessEngine.utils import Coord


class Queen(Piece):
    """
    Class of Queen
    """

    def get_moves(self, pos: Coord, board):
        """
        Return all moves from current position
        """
        rook = Rook(self.color)
        for move in rook.get_moves(pos, board):
            yield move
        bishop = Bishop(self.color)
        for move in bishop.get_moves(pos, board):
            yield move

    def get_attack(self, pos: Coord, board):
        """
        Return all attack moves from current position
        """
        rook = Rook(self.color)
        for move in rook.get_attack(pos, board):
            yield move
        bishop = Bishop(self.color)
        for move in bishop.get_attack(pos, board):
            yield move


