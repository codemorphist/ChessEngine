from chess import *
from graphic import draw_board

chess = Chess("8/8/8/8/8/3k4/2P3P1/8 w - - 0 1")

draw_board(chess)

bk = chess._kings[Color.BLACK]
print(algebraic(bk))

print(chess._attacked(bk, Color.WHITE))

print()
