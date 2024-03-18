from chess import *
from engine import find_mat_two
from graphic import draw_board


fen = input()
chess = Chess(fen)
draw_board(chess)

for mat in find_mat_two(fen):
    for m in mat:
        print(m)
    print(10 * "-")
