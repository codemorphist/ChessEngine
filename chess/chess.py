from enum import Enum, auto

class Color(Enum):
    WHITE = "w"
    BLACK = "b"
    
class Piece(Enum):
    PAWN = "p"
    KNIGHT = "n"
    BISHOP = "b"
    ROOK = "r"
    QUEEN = "q"
    KING = "k"

X88 = {
  "a8":   0, "b8":   1, "c8":   2, "d8":   3, "e8":   4, "f8":   5, "g8":   6, "h8":   7,
  "a7":  16, "b7":  17, "c7":  18, "d7":  19, "e7":  20, "f7":  21, "g7":  22, "h7":  23,
  "a6":  32, "b6":  33, "c6":  34, "d6":  35, "e6":  36, "f6":  37, "g6":  38, "h6":  39,
  "a5":  48, "b5":  49, "c5":  50, "d5":  51, "e5":  52, "f5":  53, "g5":  54, "h5":  55,
  "a4":  64, "b4":  65, "c4":  66, "d4":  67, "e4":  68, "f4":  69, "g4":  70, "h4":  71,
  "a3":  80, "b3":  81, "c3":  82, "d3":  83, "e3":  84, "f3":  85, "g3":  86, "h3":  87,
  "a2":  96, "b2":  97, "c2":  98, "d2":  99, "e2": 100, "f2": 101, "g2": 102, "h2": 103,
  "a1": 112, "b1": 113, "c1": 114, "d1": 115, "e1": 116, "f1": 117, "g1": 118, "h1": 119
}

BOARD = [X88[key] for key in X88.keys()]
    
PAWN_OFFSETS = {
  Color.BLACK: [16, 32, 17, 15],
  Color.WHITE: [-16, -32, -17, -15],
}

RANK_1 = 7
RANK_2 = 6
RANK_3 = 5
RANK_4 = 4
RANK_5 = 3
RANK_6 = 2
RANK_7 = 1
RANK_8 = 0

SECOND_RANK = { Color.BLACK: RANK_7, Color.WHITE: RANK_2 }


PIECE_OFFSETS = {
  Piece.KNIGHT: [-18, -33, -31, -14, 18, 33, 31, 14],
  Piece.BISHOP: [-17, -15, 17, 15],
  Piece.ROOK: [-16, 1, 16, -1],
  Piece.QUEEN: [-17, -16, -15, 1, 17, 16, 15, -1],
  Piece.KING: [-17, -16, -15, 1, 17, 16, 15, -1],
}

ATTACKS = [
  20, 0, 0, 0, 0, 0, 0, 24,  0, 0, 0, 0, 0, 0,20, 0,
   0,20, 0, 0, 0, 0, 0, 24,  0, 0, 0, 0, 0,20, 0, 0,
   0, 0,20, 0, 0, 0, 0, 24,  0, 0, 0, 0,20, 0, 0, 0,
   0, 0, 0,20, 0, 0, 0, 24,  0, 0, 0,20, 0, 0, 0, 0,
   0, 0, 0, 0,20, 0, 0, 24,  0, 0,20, 0, 0, 0, 0, 0,
   0, 0, 0, 0, 0,20, 2, 24,  2,20, 0, 0, 0, 0, 0, 0,
   0, 0, 0, 0, 0, 2,53, 56, 53, 2, 0, 0, 0, 0, 0, 0,
  24,24,24,24,24,24,56,  0, 56,24,24,24,24,24,24, 0,
   0, 0, 0, 0, 0, 2,53, 56, 53, 2, 0, 0, 0, 0, 0, 0,
   0, 0, 0, 0, 0,20, 2, 24,  2,20, 0, 0, 0, 0, 0, 0,
   0, 0, 0, 0,20, 0, 0, 24,  0, 0,20, 0, 0, 0, 0, 0,
   0, 0, 0,20, 0, 0, 0, 24,  0, 0, 0,20, 0, 0, 0, 0,
   0, 0,20, 0, 0, 0, 0, 24,  0, 0, 0, 0,20, 0, 0, 0,
   0,20, 0, 0, 0, 0, 0, 24,  0, 0, 0, 0, 0,20, 0, 0,
  20, 0, 0, 0, 0, 0, 0, 24,  0, 0, 0, 0, 0, 0,20
]

RAYS = [
   17,  0,  0,  0,  0,  0,  0, 16,  0,  0,  0,  0,  0,  0, 15, 0,
    0, 17,  0,  0,  0,  0,  0, 16,  0,  0,  0,  0,  0, 15,  0, 0,
    0,  0, 17,  0,  0,  0,  0, 16,  0,  0,  0,  0, 15,  0,  0, 0,
    0,  0,  0, 17,  0,  0,  0, 16,  0,  0,  0, 15,  0,  0,  0, 0,
    0,  0,  0,  0, 17,  0,  0, 16,  0,  0, 15,  0,  0,  0,  0, 0,
    0,  0,  0,  0,  0, 17,  0, 16,  0, 15,  0,  0,  0,  0,  0, 0,
    0,  0,  0,  0,  0,  0, 17, 16, 15,  0,  0,  0,  0,  0,  0, 0,
    1,  1,  1,  1,  1,  1,  1,  0, -1, -1,  -1,-1, -1, -1, -1, 0,
    0,  0,  0,  0,  0,  0,-15,-16,-17,  0,  0,  0,  0,  0,  0, 0,
    0,  0,  0,  0,  0,-15,  0,-16,  0,-17,  0,  0,  0,  0,  0, 0,
    0,  0,  0,  0,-15,  0,  0,-16,  0,  0,-17,  0,  0,  0,  0, 0,
    0,  0,  0,-15,  0,  0,  0,-16,  0,  0,  0,-17,  0,  0,  0, 0,
    0,  0,-15,  0,  0,  0,  0,-16,  0,  0,  0,  0,-17,  0,  0, 0,
    0,-15,  0,  0,  0,  0,  0,-16,  0,  0,  0,  0,  0,-17,  0, 0,
  -15,  0,  0,  0,  0,  0,  0,-16,  0,  0,  0,  0,  0,  0,-17
]


PIECE_MASKS = { 
    Piece.PAWN: 0x1, 
    Piece.KNIGHT: 0x2, 
    Piece.BISHOP: 0x4, 
    Piece.ROOK: 0x8, 
    Piece.QUEEN: 0x10, 
    Piece.KING: 0x20 
}

DEFAULT_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w"

def rank(square: int) -> int:
    return square >> 4


def file(square: int) -> int:
    return square & 0x0f


def algebraic(square: int) -> str:
    f = file(square)
    r = rank(square)
    return f"{chr(ord('a')+f)}{8-r}"

def numeric(square: str) -> int:
    return X88[square]


def swap_color(color: Color) -> Color:
    return Color.WHITE if color is Color.BLACK else Color.BLACK


def get_piece_color(piece: str) -> Color:
    return Color.BLACK if piece.islower() else Color.WHITE


def get_piece_type(piece: str) -> Piece:
    return Piece(piece.lower()) 

class Move:
    def __init__(self, piece: Piece, color: Color, f: int, t: int):
        self._piece = piece
        self._color = color
        self._from = f
        self._to = t

    def __str__(self) -> str:
        piece = self._piece.name
        f = algebraic(self._from)
        t = algebraic(self._to)
        color = self._color.name
        return f"{piece} {color}  {f}-{t}"

    def __iter__(self):
        yield self._from
        yield self._to

class Chess:
    def __init__(self, fen: str = DEFAULT_FEN):
        self._board: list[str] = [None for _ in range(128)]
        self._turn: Color = None
        self._kings: dict[Color, int] = { Color.WHITE: None, Color.BLACK: None }
        self._history: list[Moves] = []

        self._load(fen)

    def _load(self, fen: str) -> None:
        self._board = [None for _ in range(128)]

        fen = fen.split(" ")

        square = 0
        for ch in fen[0]:
            if ch == "/":
                square += 8           
                continue

            if square & 0x88 != 0:
                square += 7
                continue

            if ch.isnumeric():
                square += int(ch)
                continue

            # save king position
            if get_piece_type(ch) == Piece.KING:
                self._kings[get_piece_color(ch)] = square

            self._board[square] = ch

            square += 1

        self._turn = Color(fen[1])

    def put(self, pos: str, piece: Piece, color: Color):
        piece_symbol = piece.value
        piece_symbol = piece_sumbol.uppper() if color == Color.WHITE else piece_symbol
        coord = X88[pos]
        self._board[coord] = piece_symbol

    def _get(self, pos: int) -> str:
        fig = self._board[pos]
        return fig if fig is not None else " "

    def get(self, pos: str) -> str:
        return self.get(numeric(pos))

    def _attacked(self, square: int, color: Color) -> bool:
        if square & 0x88:
            return False

        for pos in BOARD:
            piece = self._board[pos]

            if piece is None:
                continue

            piece_type = get_piece_type(piece)
            piece_color = get_piece_color(piece)

            if piece_color != color:
                continue

            difference = pos - square

            if difference == 0:
                continue

            index = difference + 119
            if ATTACKS[index] & PIECE_MASKS[piece_type]:
                if piece_type == Piece.PAWN:
                    if difference < 0:
                        if piece_color == Color.WHITE:
                            return True
                    else:
                        if piece_color == Color.BLACK:
                            return True
                    continue

                if piece_type == Piece.KNIGHT or piece_type == Piece.KING:
                    return True

                offset = RAYS[index]
                j = pos + offset
                
                blocked = False
                while j != square:
                    if self._board[j] is not None:
                        blocked = True
                        break
                    j += offset
                if not blocked: 
                    return True

            
        return False

    def _update(self):
        for square in BOARD:
            piece = self._board[square]
            if piece is None:
                continue

            if get_piece_type(piece) == Piece.KING:
                self._kings[get_piece_color(piece)] = square
 
    def _move(self, move: Move):
        f, t = move 
        piece = self._board[f]
        self._board[f] = None
        self._board[t] = piece
        self._history.append(move)
        self._update()

    def move(self, f: str, t: str):
        fn = numeric(f)
        tn = numeric(t)
        piece_type = get_piece_type(self._board[fn])
        piece_color = get_piece_color(self._board[fn])
        self._move(Move(piece_type, piece_color, fn, tn))

    def undo(self):
        f, t = self._history.pop()
        piece = self._board[t]
        self._board[t] = None
        self._board[f] = piece
        self._update()

    def _moves(self,
               for_piece: Piece = None, 
               for_square: int = None, 
               legal: bool = True) -> list[Move]:
        moves: list[Move] = []

        first_square = X88["a8"]
        last_square = X88["h1"]
        us = self._turn
        them = swap_color(us)
    
        if for_square is not None:
            if not (for_square & 0x88):
                return []
            else:
                first_square = for_square
                last_square = for_square
            
        pos = first_square-1
        while pos <= last_square:
            pos += 1
            if pos & 0x88:
                pos += 7
                continue

            piece = self._board[pos] 
            if piece is None or get_piece_color(piece) == them:
                continue
            
            piece_type = get_piece_type(piece)

            if (for_piece and for_piece != piece_type):
                continue

            to: int = None
            if piece_type == Piece.PAWN:
                # default moves
                to = pos + PAWN_OFFSETS[us][0]
                if self._board[to] is None:
                    moves.append(
                        Move(piece_type, us, pos, to)
                    )

                    to = pos + PAWN_OFFSETS[us][1]
                    if SECOND_RANK[us] == rank(pos) and self._board[to] is None:
                        moves.append(
                            Move(piece_type, us, pos, to)
                        )

                # captures
                for j in range(2, 4):
                    to = pos + PAWN_OFFSETS[us][j]
                    
                    if to & 0x88:
                        continue

                    atk_fig = self._board[to]
                    if atk_fig is not None and get_piece_color(atk_fig) == them:
                        moves.append(
                            Move(piece_type, us, pos, to)
                        )
                    else: # for passant
                        ... 
            else: # for other pieces
                for off in PIECE_OFFSETS[piece_type]:
                    to = pos

                    while True:
                        to += off

                        if to & 0x88:
                            break

                        atk_fig = self._board[to]
                        
                        if atk_fig is None:
                            moves.append(
                                Move(piece_type, us, pos, to)
                            )
                        else:
                            if get_piece_color(atk_fig) == us:
                                break

                            moves.append(
                                Move(piece_type, us, pos, to)
                            )
                            break

                        if piece_type == Piece.KNIGHT or \
                           piece_type == Piece.KING:
                            break

        # castling
        # ...

        if not legal:
            return moves

        legal_moves = []
        for m in moves:
            self._move(m)
            if not self._is_king_attacked(us):
                legal_moves.append(m)
            self.undo()

        return legal_moves

    def is_attacked(self, square: str, color: Color) -> bool:
        square = numeric(square)
        return self._attacked(square, color)

    def _is_king_attacked(self, color: Color) -> bool:
        return self._attacked(self._kings[color], swap_color(color))

    def is_check(self) -> bool:
        return _is_king_attacked() 

    def is_checkmate(self) -> bool:
        return self.is_check() and not len(self._moves())

    def is_statemate(self) -> bool:
        return not self.is_check() and not len(self._moves())

    @property
    def board(self) -> list[list[str]]:
        board = []
        row = []
        count = 0
        for sq in BOARD:
            row.append(self._get(sq))            
            count += 1
            if (sq + 1) % 8 == 0:
                board.append(row)
                row = []
        return board

    def ascii(self) -> str:
        board = ""
        count = 0
        for sq in BOARD:
            if file(sq) == 0:
                board += f"{8-rank(sq)}  "
            fig = self._board[sq]
            count += 1
            board += (fig if fig is not None else "_") + " "
            if (sq + 1) % 8 == 0:
                board += "\n"
        board += "   a b c d e f g h"
        return board

    
        
