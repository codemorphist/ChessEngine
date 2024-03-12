from ChessEngine.chess import Chess
from ChessEngine.utils import Coord
from ChessEngine.utils.enums import Color
from ChessEngine.pieces import Pawn
from ChessEngine.graphic import ascii, draw_board

c = Chess()
draw_board(c)
