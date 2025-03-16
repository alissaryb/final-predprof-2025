import json

from backend.src.api_requests import get_all_tiles

cnt2 = 4
cnt = 16
sz = 64
A = 256

def get_mat(tile):
    mat = [[0] * cnt2 for i in range(cnt2)]
    for i in range(cnt):
        top = tile[i][0][sz // 2] == 255
        bottom = tile[i][sz - 1][sz // 2] == 255
        left = tile[i][sz // 2][0] == 255
        right = tile[i][sz // 2][sz - 1] == 255
        if top and left:
            mat[0][0] = i
        elif top and right:
            mat[0][cnt2 - 1] = i
        elif bottom and left:
            mat[cnt2 - 1][0] = i
        elif bottom and right:
            mat[cnt2 - 1][cnt2 - 1] = i
        elif not top and not bottom and not right and not left:
            if tile[i][0][0] == 0:
                mat[2][2] = i
            elif tile[i][0][sz - 1] == 0:
                mat[2][1] = i
            elif tile[i][sz - 1][0] == 0:
                mat[1][2] = i
            else:
                mat[1][1] = i
    for i in range(cnt):
        top = tile[i][0][sz // 2] == 255
        bottom = tile[i][sz - 1][sz // 2] == 255
        left = tile[i][sz // 2][0] == 255
        right = tile[i][sz // 2][sz - 1] == 255
        if top and left:
            pass
        elif top and right:
            pass
        elif bottom and left:
            pass
        elif bottom and right:
            pass
        elif not top and not bottom and not right and not left:
            pass
        else:
            if top:
                diff1 = 0
                diff2 = 0
                for k in range(sz):
                    diff1 += tile[mat[0][0]][k][sz - 1] - tile[i][k][0]
                    diff2 += tile[mat[0][3]][k][0] - tile[i][k][sz - 1]
                if diff1 < diff2:
                    mat[0][1] = i
                else:
                    mat[0][2] = i
            elif bottom:
                diff1 = 0
                diff2 = 0
                for k in range(sz):
                    diff1 += tile[mat[3][0]][k][sz - 1] - tile[i][k][0]
                    diff2 += tile[mat[3][3]][k][0] - tile[i][k][sz - 1]
                if diff1 < diff2:
                    mat[3][1] = i
                else:
                    mat[3][2] = i
            elif right:
                diff1 = 0
                diff2 = 0
                for k in range(sz):
                    diff1 += tile[mat[0][0]][sz - 1][k] - tile[i][0][k]
                    diff2 += tile[mat[3][0]][0][k] - tile[i][sz - 1][k]
                if diff1 < diff2:
                    mat[1][3] = i
                else:
                    mat[2][3] = i
            elif left:
                diff1 = 0
                diff2 = 0
                for k in range(sz):
                    diff1 += tile[mat[0][3]][sz - 1][k] - tile[i][0][k]
                    diff2 += tile[mat[3][3]][0][k] - tile[i][sz - 1][k]
                if diff1 < diff2:
                    mat[1][0] = i
                else:
                    mat[2][0] = i
    return mat


def get_field():
    tiles = get_all_tiles()
    field = [[0] * A for i in range(A)]
    mat = get_mat(tiles)
    for ti in range(cnt2):
        for tj in range(cnt2):
            for i in range(sz):
                for j in range(sz):
                    field[ti * sz + i][tj * sz + j] = tiles[mat[ti][tj]][i][j]
    return field

# def get_tiles_from_files():
#     data = []
#     for i in range(16):
#         with open(f"tyles_files/{i + 1}.json", "r") as f:
#             relief = json.load(f)
#             data.append(relief)
#     return data


