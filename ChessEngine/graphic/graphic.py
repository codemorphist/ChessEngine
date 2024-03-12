from ChessEngine.chess import Chess
from ChessEngine.utils.enums import *
from ChessEngine.pieces import *
from ChessEngine.utils.fen import piece_to_char
from .sprites import *


def sprite(fig: Piece):
    if isinstance(fig, Pawn):
        return WHITE_PAWN if fig.color is Color.White else BLACK_PAWN
    elif isinstance(fig, Knight):
        return WHITE_KNIGHT if fig.color is Color.White else BLACK_KNIGHT
    elif isinstance(fig, Bishop):
        return WHITE_BISHOP if fig.color is Color.White else BLACK_BISHOP
    elif isinstance(fig, Rook):
        return WHITE_ROOK if fig.color is Color.White else BLACK_ROOK
    elif isinstance(fig, Queen):
        return WHITE_QUEEN if fig.color is Color.White else BLACK_QUEEN
    elif isinstance(fig, King):
        return WHITE_KING if fig.color is Color.White else BLACK_KING


def draw_board(chess: Chess):
    board = chess.board
    for y, row in enumerate(board):
        print(8 - y, end=" ")
        for x, fig in enumerate(row):
            print(WHITE_TILE_COLOR if (x + y) % 2 == 0 else BLACK_TILE_COLOR, end="")
            if fig is None:
                print(" ", end=" ")
            else:
                print(WHITE_FIGURE_COLOR if fig.color is Color.White else BLACK_FIGURE_COLOR, end="")
                print(sprite(fig), end=" ")
        print(RESET_COLOR)
    print("  ", end="")
    for i in range(8):
        print(chr(ord("a") + i), end=" ")
    print()


def ascii(chess: Chess) -> str:
    board = chess.board
    ascii_board = ""
    for y, row in enumerate(board):
        ascii_row = ""
        for fig in row:
            ascii_row += piece_to_char(fig) + " "
        ascii_board += f"{8 - y}  " + ascii_row + "\n"
    ascii_board += "   "
    for i in range(8):
        ascii_board += chr(ord("a") + i) + " "
    return ascii_board
