from ChessEngine.utils.enums import MoveType, Color
from ChessEngine.utils.coord import Coord


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
