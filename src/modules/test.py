from parser import *

my_parser = Parser("tap? inc att 2; tap? inc end 2")
result = my_parser.parse()
print(result)