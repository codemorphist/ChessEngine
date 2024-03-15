from chess import Chess, Color, Piece, Move

chess = Chess("3q4/8/8/q7/4K3/7q/8/5q2 w")

print(chess.ascii())

for m in chess._moves():
    print(m)

