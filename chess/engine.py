import os
from chess import *
from graphic import *

fen = input("Input FEN of position: ")

chess = Chess(fen)

os.system("clear")

draw_board(chess)

moves = []
for m1 in chess._moves():
    chess._move(m1)
    for m2 in chess._moves():
        chess._move(m2)
        for m3 in chess._moves():
            chess._move(m3)
            if chess.is_checkmate():
                fen = chess.fen
                moves.append((m1, m2, m3, fen))
            chess.undo()
        chess.undo()
    chess.undo()

for m1, m2, m3, fen in moves:
    os.system("clear")
    print("-"*10)
    print(m1)
    print(m2)
    print(m3)
    draw_board(Chess(fen))
    input()
    print("-"*10)
