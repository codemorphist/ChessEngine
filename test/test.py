from ChessEngine.chess import Chess
from ChessEngine.utils import Coord
from ChessEngine.utils.enums import Color
from ChessEngine.pieces import *
from ChessEngine.graphic import ascii, draw_board

c = Chess("8/8/8/8/8/8/8/8")
c.set_piece(Rook(Color.White), Coord("f4"))
c.set_piece(King(Color.Black), Coord("e6"))
attacked = [str(m) for m in c.get_moves(Coord("e6"))]
print(attacked)
draw_board(c, attacked=attacked)

