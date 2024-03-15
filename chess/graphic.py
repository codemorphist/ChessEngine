from chess import Chess
from sprites import *


def sprite(fig: str) -> str:
    color = fig.islower()
    fig = fig.lower()
    if fig == "p":
        return WHITE_PAWN if color else BLACK_PAWN
    if fig == "n":
        return WHITE_KNIGHT if color else BLACK_KNIGHT
    if fig == "b":
        return WHITE_BISHOP if color else BLACK_BISHOP
    if fig == "r":
        return WHITE_ROOK if color else BLACK_ROOK
    if fig == "q":
        return WHITE_QUEEN if color else BLACK_QUEEN
    if fig == "k":
        return WHITE_KING if color else BLACK_KING

def tile(x: int, y: int) -> str:
    if (x+y)%2 == 0:
        return WHITE_TILE_COLOR + " "
    else:
        return BLACK_TILE_COLOR + " "

def draw_board(chess: Chess, attacked=[]):
    board = chess.board
    for y, row in enumerate(board):
        print(8-y, end=" ")
        for x, piece in enumerate(row):
            print(tile(x, y), end="")
            if piece == " ":
                print("  ", end="")
            else:
                color = WHITE_FIGURE_COLOR if piece.islower() else BLACK_FIGURE_COLOR
                print(color + sprite(piece) + " ",end="")
        print(RESET_COLOR)
    print("  ", end="")
    for i in range(8):
        print("", chr(ord("a") + i), end=" ")
    print()

            

