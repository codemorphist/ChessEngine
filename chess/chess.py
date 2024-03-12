from utils.move import Move
from pieces import Piece
from utils.enums import Color
from utils.coord import Coord
from utils.fen import fen_to_board, board_to_fen


class Chess:
    def __init__(self, fen: str = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"):
        self._fen = fen
        self._board: list[list[Piece]] = fen_to_board(fen)
        self._color: Color = None
        self._hisroty: list[Move] = []

    @property
    def board(self) -> list[list[Piece]]:
        """
        :return: board
        """
        return self._board

    @property
    def fen(self) -> str:
        """
        :return: fen
        """
        self._fen = board_to_fen(self.board)
        return self._fen

    def set_piece(self, piece: Piece, pos: Coord):
        """
        Set piece to position
        :param piece: Piece to set
        :param pos: to set Piece
        """
        ...

    def get_piece(self, pos: Coord) -> Piece:
        """
        Get piece from position

        :param pos: with Piece
        :return: Piece from pos
        """
        ...
