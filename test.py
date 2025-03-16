import json

tile = []

cnt = 16
sz = 64
for i in range(1, cnt + 1):
    tile.append(json.loads(open(f"backend/tyles_files/{i}.json").read()))

for i in range(cnt):
    with open(f"out/{i}.txt", "w") as f:
        for j in range(sz):
            f.write(str(tile[i][j]))
            f.write("\n")

# top = [-1] * cnt
# bottom = [-1] * cnt
# right = [-1] * cnt
# left = [-1] * cnt
# for i in range(0, cnt):
#     mindiff = 1e18
#     mindiffj = -1
#     for j in range(0, cnt):
#         if i == j:
#             continue
#         diff = 0
#         for k in range(sz):
#             cand = abs(tile[i][0][k] - tile[j][sz - 1][k])
#             if cand < mindiff:
#                 mindiff = cand
#                 mindiffj = j
#     top[i] = mindiffj
#     bottom[mindiffj] = i
# for i in range(0, cnt):
#     mindiff = 1e18
#     mindiffj = -1
#     for j in range(0, cnt):
#         if i == j:
#             continue
#         diff = 0
#         for k in range(sz):
#             cand = abs(tile[i][k][0] - tile[j][k][sz - 1])
#             if cand < mindiff:
#                 mindiff = cand
#                 mindiffj = j
#     left[i] = mindiffj
#     right[mindiffj] = i
#
# for i in range(cnt):
#     print("top", i, top[i])
