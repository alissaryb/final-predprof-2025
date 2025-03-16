import json

tile = []

cnt = 16
cnt2 = 4
sz = 64
for i in range(1, cnt + 1):
    tile.append(json.loads(open(f"backend/tyles_files/{i}.json").read()))

