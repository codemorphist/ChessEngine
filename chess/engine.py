from time import time
from copy import copy, deepcopy

from chess import *
from graphic import draw_board

PAWN_C = [  0,  0,  0,  0,  0,  0,  0,  0,
            50, 50, 50, 50, 50, 50, 50, 50,
            10, 10, 20, 30, 30, 20, 10, 10,
            5,  5, 10, 25, 25, 10,  5,  5,
            0,  0,  0, 20, 20,  0,  0,  0,
            5, -5,-10,  0,  0,-10, -5,  5,
            5, 10, 10,-20,-20, 10, 10,  5,
            0,  0,  0,  0,  0,  0,  0,  0]

KNIGHT_C = [-50,-40,-30,-30,-30,-30,-40,-50,
            -40,-20,  0,  0,  0,  0,-20,-40,
            -30,  0, 10, 15, 15, 10,  0,-30,
            -30,  5, 15, 20, 20, 15,  5,-30,
            -30,  0, 15, 20, 20, 15,  0,-30,
            -30,  5, 10, 15, 15, 10,  5,-30,
            -40,-20,  0,  5,  5,  0,-20,-40,
            -50,-40,-30,-30,-30,-30,-40,-50]

BISHOP_C = [-20,-10,-10,-10,-10,-10,-10,-20,
            -10,  0,  0,  0,  0,  0,  0,-10,
            -10,  0,  5, 10, 10,  5,  0,-10,
            -10,  5,  5, 10, 10,  5,  5,-10,
            -10,  0, 10, 10, 10, 10,  0,-10,
            -10, 10, 10, 10, 10, 10, 10,-10,
            -10,  5,  0,  0,  0,  0,  5,-10,
            -20,-10,-10,-10,-10,-10,-10,-20]

ROOK_C = [  0,  0,  0,  0,  0,  0,  0,  0,
            5, 10, 10, 10, 10, 10, 10,  5,
            -5,  0,  0,  0,  0,  0,  0, -5,
            -5,  0,  0,  0,  0,  0,  0, -5,
            -5,  0,  0,  0,  0,  0,  0, -5,
            -5,  0,  0,  0,  0,  0,  0, -5,
            -5,  0,  0,  0,  0,  0,  0, -5,
             0,  0,  0,  5,  5,  0,  0,  0]

QUEEN_C = [ -20,-10,-10, -5, -5,-10,-10,-20,
            -10,  0,  0,  0,  0,  0,  0,-10,
            -10,  0,  5,  5,  5,  5,  0,-10,
            -5,  0,  5,  5,  5,  5,  0, -5,
             0,  0,  5,  5,  5,  5,  0, -5,
            -10,  5,  5,  5,  5,  5,  0,-10,
            -10,  0,  5,  0,  0,  0,  0,-10,
            -20,-10,-10, -5, -5,-10,-10,-20]

KING_C = [-20,-10,-10, -5, -5,-10,-10,-20,
        -10,  0,  0,  0,  0,  0,  0,-10,
        -10,  0,  5,  5,  5,  5,  0,-10,
        -5,  0,  5,  5,  5,  5,  0, -5,
        0,  0,  5,  5,  5,  5,  0, -5,
        -10,  5,  5,  5,  5,  5,  0,-10,
        -10,  0,  5,  0,  0,  0,  0,-10,
        -20,-10,-10, -5, -5,-10,-10,-20]


def evaulate(chess: Chess) -> int:
    points = 0

    sign = 1 if chess._turn == Color.WHITE else -1

    if chess.is_checkmate():
        points += 9999
    elif chess.is_check():
        points += -9999999999999

    for y, row in enumerate(chess.board):
        for x, piece in enumerate(row):
            if piece == " ":
                continue
            s = 1 if piece.isupper() else -1
            if sign != s:
                continue
            index = 8*y + x
            if sign != 1:
                index = (7-y)*8 + x

            match piece.lower():
                case "p":
                    points += 10 # + PAWN_C[index]
                case "n":
                    points += 30 # + KNIGHT_C[index]
                case "b":
                    points += 30 # + KNIGHT_C[index]
                case "r":
                    points += 50 # + ROOK_C[index]
                case "q":
                    points += 90 # + QUEEN_C[index]
                case "k":
                    points += 900 # + KING_C[index]
    return sign*points


def minimax(chess: Chess, a: int, b: int, maximizing_player, depth):
    if depth < 0:
        return -evaulate(chess)

    best_move = None
    if maximizing_player:
        best_move = -9999
    else:
        best_move = 9999

    for move in chess._moves():
        chess._move(move)
        if maximizing_player:
            best_move = max(best_move, minimax(chess, a, b, False, depth-1))
            chess.undo()
            a = max(a, best_move)
            if b <= a:
                return best_move
        else:
            best_move = min(best_move, minimax(chess, a, b, True, depth-1))
            chess.undo()
            b = min(b, best_move)
            if b <= a:
                return best_move
    return best_move


def minimax_root(chess: Chess, maximizing_player=True, depth=2):
    best_move_found: Move = None
    best_move: float = -9999

    maximizing_player = chess._turn != Color.WHITE

    for move in chess._moves():
        chess._move(move)
        value = minimax(chess, -10000, 10000, not maximizing_player, depth-1)
        chess.undo()
        if value >= best_move:
            best_move_found = move
            best_move = value

    return best_move_found


def calc(chess: Chess, max_depth=2) -> Move:
    return minimax_root(chess, False, depth=max_depth)


def find_mat_two(fen: str):
    chess = Chess(fen)

    mat_two = []
    for m1 in chess._moves():
        chess._move(m1)
        for m2 in chess._moves():
            chess._move(m2)
            for m3 in chess._moves():
                chess._move(m3)
                if chess.is_checkmate():
                    mat_two += [[m1, m2, m3]]
                chess.undo()
            chess.undo()
        chess.undo()

    return mat_two


