import backend.tiles
import json
import backend.algorithm
from backend.algorithm import calc_pos

from backend.tiles import *

tile = []

cnt = 16
cnt2 = 4
sz = 64
for i in range(1, cnt + 1):
    tile.append(json.loads(open(f"backend/tyles_files/{i}.json").read()))
print("ok")
print(calc_pos(get_field(tile), 10, 10, 200, 200, 30, 1, 60, 2))

# print(get_mat(tile))
# field = get_field(tile)
# with open("out/test.txt", "w") as f:
#     for i in range(256):
#         f.write(str(field[i]))
#         f.write("\n")

