from parser import *

parser = Parser("entertap; tap? for 1 blue gen 1 green; tap? gen 1 blue")
print(parser.parse())
