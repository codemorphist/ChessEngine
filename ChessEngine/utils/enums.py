from enum import Enum, auto


class Color(Enum):
    White = auto()
    Black = auto()


class MoveType(Enum):
    Move = auto()
    Attack = auto()
    Check = auto()
    Mat = auto()
    Pat = auto()
    # TODO
    Passant = auto()
    Castling = auto()
