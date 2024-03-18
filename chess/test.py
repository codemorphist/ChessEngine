from chess import *
from engine import find_mat_two
from graphic import draw_board


fen = "r2qkb1r/pp2nppp/3p4/2pNN1B1/2BnP3/3P4/PPP2PPP/R2bK2R w KQkq - 1 0"
chess = Chess(fen)
draw_board(chess)

for mat in find_mat_two(fen):
    for m in mat:
        print(m)
    print(10 * "-")
