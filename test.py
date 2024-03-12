from utils import Coord, Line

l = Line(Coord("a8"), Coord("h1"))

print(l.on_line(Coord("g3")))
