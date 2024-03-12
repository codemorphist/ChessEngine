from ChessEngine.pieces import Piece
from ChessEngine.utils import Coord
from ChessEngine.utils.checkers import on_board, can_move
from ChessEngine.utils.enums import Color


def king_near(color: Color, pos: Coord, board: list[list[Piece]]) -> bool:
    x, y = pos

    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if not on_board(Coord(i, j)):
                continue
            fig = board[j][i]
            if isinstance(fig, King) or fig.color is not color:
                return True
    return False


class King(Piece):
    """
    Class of King
    """

    def get_moves(self, pos: Coord, board):
        """
        Return all moves from current position
        """
        x, y = pos
        for i in range(x+1, x+2):
            for j in range(y+1, y+2):
                coord = Coord(i, j)
                if on_board(coord) and can_move(coord, board):
                    yield Coord

    def get_attack(self, pos: Coord, board):
        """
        Return all attack moves from current position
        """
        yield None
