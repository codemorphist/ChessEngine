from ChessEngine.pieces import *
from ChessEngine.utils.enums import Color


def piece_to_char(piece: Piece) -> str:
    """
    Convert piece to char in fen notation
    :param piece: piece to convert
    :return: char of piece
    """
    if isinstance(piece, Pawn):
        return "P" if piece.color is Color.White else "p"
    elif isinstance(piece, Knight):
        return "N" if piece.color is Color.White else "n"
    elif isinstance(piece, Bishop):
        return "B" if piece.color is Color.White else "b"
    elif isinstance(piece, Rook):
        return "R" if piece.color is Color.White else "r"
    elif isinstance(piece, Queen):
        return "Q" if piece.color is Color.White else "q"
    elif isinstance(piece, King):
        return "K" if piece.color is Color.White else "k"
    else:
        return " "


def board_to_fen(board: list[list[Piece]]) -> str:
    """
    Convert board to FEN string
    :param board: array of _pieces
    :return: chess position in FEN notation
    """
    ...


def char_to_piece(ch: str) -> Piece:
    """

    :param ch: symbol of piece
    :return: Piece object
    """
    col: Color = Color.Black if ch.islower() else Color.White
    match ch.lower():
        case "p":
            return Pawn(col)
        case "n":
            return Knight(col)
        case "b":
            return Bishop(col)
        case "r":
            return Rook(col)
        case "q":
            return Queen(col)
        case "k":
            return King(col)


def fen_to_board(fen: str) -> list[list[Piece]]:
    """
    Convert FEN to array of _pieces
    
    About FEN: https://www.chessprogramming.org/Forsyth-Edwards_Notation

    <FEN> ::=  <Piece Placement>
       ' ' <Side to move>
       ' ' <Castling ability>
       ' ' <En passant target square>
       ' ' <Halfmove clock>
       ' ' <Fullmove counter>

    :param fen: position in FEN notation
    :return: 2D array of _pieces
    """
    fen = fen.split()

    board: list[list[Piece]] = []
    for row in fen[0].split("/"):
        r = []
        for figure in row:
            if figure.isnumeric():
                r += [None for _ in range(int(figure))]
            else:
                r.append(char_to_piece(figure))
        board.append(r)
    return board
