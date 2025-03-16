import backend.tiles
import json

from backend.tiles import *

tile = []

cnt = 16
cnt2 = 4
sz = 64
for i in range(1, cnt + 1):
    tile.append(json.loads(open(f"backend/tyles_files/{i}.json").read()))

print(get_mat(tile))
field = get_field(tile)
with open("out/test.txt", "w") as f:
    for i in range(256):
        f.write(str(field[i]))
        f.write("\n")
