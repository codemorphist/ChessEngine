from ChessEngine.pieces import Piece
from ChessEngine.utils import Coord
from ChessEngine.utils.checkers import can_move, can_attack


class Rook(Piece):
    """
    Class of Rook
    """

    def get_moves(self, pos: Coord, board, attack: bool = False):
        """
        Return all moves from current position
        """
        x, y = pos
        for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            c = 1
            coord = Coord(x + i * c, y + j * c)
            while can_move(coord, board) \
                    or (attack and can_attack(self, coord, board)):
                if attack and can_attack(self, coord, board):
                    yield coord
                    break
                yield coord
                c += 1
                coord = Coord(x + i * c, y + j * c)

    def get_attack(self, pos: Coord, board):
        """
        Return all attack moves from current position
        """
        return self.get_moves(pos, board, True)