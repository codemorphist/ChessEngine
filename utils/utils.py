class Coord:
    def __init__(self, *args):
        if len(args) == 1:  # in algebraic form
            self.x, self.y = self._to_coord(args[0])
        elif len(args) == 2:  # in standard form
            self.x = args[0]
            self.y = args[1]

    @property
    def algebraic(self) -> str:
        """
        :return Coords in algebraic notation
        """
        file = chr(ord("a") + self.x)
        rank = 8 - self.y
        return f"{file}{rank}"

    @staticmethod
    def _to_coord(self, alg: str) -> tuple[int, int]:
        """
        Convert algebraic notation to coordinates
        """
        file, rank = alg
        x = int(ord(file) - ord("a"))
        y = 8 - int(rank)
        return x, y

    def __iter__(self):
        yield self.x
        yield self.y


class Line:
    def __init__(self, start: Coord, end: Coord):
        self.start = start
        self.end = end

    def on_line(self, pos: Coord) -> bool:
        """
        Calculate current position is on line

        :param pos position to check

        :return True if on line else False
        """
        x, y = pos.x, pos.y
        x1, y1 = self.start.x, self.start.y
        x2, y2 = self.end.x, self.end.y
        return (y2 - y1) * (x - x1) - (x2 - x1) * (y - y1) == 0
