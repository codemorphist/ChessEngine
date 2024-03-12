from utils.coord import Coord


class Line:
    def __init__(self, start: Coord, end: Coord):
        self.start = start
        self.end = end

    def on_line(self, pos: Coord) -> bool:
        """
        Calculate current position is on line

        :param pos position to check

        :return True if pos on line else False
        """
        x, y = pos.x, pos.y
        x1, y1 = self.start.x, self.start.y
        x2, y2 = self.end.x, self.end.y
        return (y2 - y1) * (x - x1) - (x2 - x1) * (y - y1) == 0
