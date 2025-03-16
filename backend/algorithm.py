import heapq

from random import randint

size = 256
cnt = 50


def calc_pos(field, from_i, from_j, to_i, to_j, r1, c1, r2, c2):
    print("Расстановка вышек...")
    g = [[[[] for _ in range(2)] for j in range(size)] for i in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(cnt):
                ei = randint(i - 120, i + 120)
                ej = randint(j - 120, j + 120)
                if ei < 0 or ei >= size or ej < 0 or ej >= size:
                    continue
                dist = ((ei - i) ** 2 + (ej - j) ** 2 + (field[i][j] - field[ei][ej]) ** 2) ** 0.5
                if dist < r1 + r1:
                    g[i][j][0].append((ei, ej, 0, c1))
                if dist < r1 + r2:
                    g[i][j][0].append((ei, ej, 1, c2))
                if dist < r2 + r1:
                    g[i][j][1].append((ei, ej, 0, c1))
                if dist < r2 + r2:
                    g[i][j][1].append((ei, ej, 1, c2))
    heap = []
    dist = [[[1e18 for _ in range(2)] for j in range(size)] for i in range(size)]
    prev = [[[(-1, -1, -1) for _ in range(2)] for j in range(size)] for i in range(size)]
    dist[from_i][from_j][0] = c1
    dist[from_i][from_j][1] = c2
    heapq.heappush(heap, (c1, from_i, from_j, 0))
    heapq.heappush(heap, (c2, from_i, from_j, 1))
    while len(heap) > 0:
        i = heap[0][1]
        j = heap[0][2]
        k = heap[0][3]
        heapq.heappop(heap)
        for (child_i, child_j, child_k, w) in g[i][j][k]:
            if dist[child_i][child_j][child_k] > dist[i][j][k] + w:
                dist[child_i][child_j][child_k] = dist[i][j][k] + w
                prev[child_i][child_j][child_k] = (i, j, k)
                heapq.heappush(heap, (dist[child_i][child_j][child_k], child_i, child_j, child_k))
    ans = 1e18
    respath = None
    for k in range(2):
        cand = dist[to_i][to_j][k]
        path = []
        cur_i = to_i
        cur_j = to_j
        cur_k = k
        while cur_i != -1:
            path.append((cur_i, cur_j, cur_k))
            (cur_i, cur_j, cur_k) = prev[cur_i][cur_j][cur_k]
        if cand < ans:
            ans = cand
            respath = path
    respath.reverse()
    print("Вышки расставлены.", respath)
    return respath
