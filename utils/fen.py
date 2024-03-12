from pieces import *
from utils.enums import Color


def piece_to_char(piece: Piece) -> str:
    """
    Convert piece to char in fen notation
    :param piece: piece to convert
    :return: char of piece
    """
    ...


def board_to_fen(board: list[list[Piece]]) -> str:
    """
    Convert board to FEN string
    :param board: array of pieces
    :return: chess position in FEN notation
    """
    ...


def char_to_piece(ch: str) -> Piece:
    """

    :param ch: symbol of piece
    :return: Piece object
    """
    color: Color = Color.White if ch.islower() else Color.Black
    match ch.lower():
        case "p":
            return Pawn(color)
        case "n":
            return Knight(color)
        case "b":
            return Bishop(color)
        case "r":
            return Rook(color)
        case "q":
            return Queen(color)
        case "k":
            return King(color)


def fen_to_board(fen: str) -> list[list[Piece]]:
    """
    Convert FEN to array of pieces
    
    About FEN: https://www.chessprogramming.org/Forsyth-Edwards_Notation

    <FEN> ::=  <Piece Placement>
       ' ' <Side to move>
       ' ' <Castling ability>
       ' ' <En passant target square>
       ' ' <Halfmove clock>
       ' ' <Fullmove counter>

    :param fen: position in FEN notation
    :return: 2D array of pieces
    """
    fen = fen.split()

    board: list[list[Piece]] = []
    for row in fen[0].split("/"):
        r = []
        for piece in row:
            if piece.isalpha():
                r += [None for _ in range(int(piece))]
            else:
                r.append(char_to_piece(piece))
        board.append(r)
    return board
