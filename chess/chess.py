from pieces import *
from utils.enums import Color, MoveType
from utils.utils import Coord


class Move:
    def __init__(self, 
                 old_fen: str,
                 new_fen: str,
                 from_pos: Coord, 
                 to_pos: Coord, 
                 color: Color,
                 move_type: MoveType):
        self.old_fen: str = old_fen
        self.new_fen: str = new_fen
        self.from_pos: Coord = from_pos 
        self.to_pos: Coord = to_pos
        self.color: Color = color
        self.move_type: MoveType = move_type


class Chess:
    def __init__(self, fen: str):
        self._fen = fen
        self._board: list[list[Piece]] = self.import_fen(fen)
        self._color: Color = color 
        self._hisroty: list[Move] = []

    @property
    def board(self) -> list[list[Piece]]:
        """
        :return board
        """
        return self._board

    @property
    def fen(self) -> str:
        """
        :return fen
        """
        return self._fen
    
    def import_fen(self, str) -> list[list[Piece]]:
        """
        Load position from FEN

        :return return array of pieces
        """
        ...

    def export_fen(self) -> str:
        """
        Export FEN of current position

        :reuturn FEN str of current position
        """
        ...

    def set_piece(self, piece: Piece, pos: Coord):
        """
        Set piece to position

        :param piece Piece to set
        :param pos to set Piece
        """
        ...

    def get_piece(self, pos: Coord) -> Piece:
        """
        Get piece from position

        :param pos with Piece

        :return Piece from pos
        """
        ...
