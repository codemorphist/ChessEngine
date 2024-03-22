from chess import *
from engine import find_mat_two
from graphic import draw_board

import time
from datetime import timedelta


fen = input("Input FEN of chess position: ")
chess = Chess(fen)
draw_board(chess)

start = time.time()

for mat in find_mat_two(fen):
    for m in mat:
        print(m)
    print(10 * "-")

end = time.time()
print("Elapsed time:", timedelta(seconds=end-start))
