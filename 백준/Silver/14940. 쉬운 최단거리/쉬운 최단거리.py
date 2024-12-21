# 쉬운 최단거리
import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int,input().split())
graph = []
dist = [[-2] * m for _ in range(n)]

for i in range(n):
    row = list(map(int,input().split()))
    for j in range(m):
        if row[j] == 0:
            dist[i][j] = 0
        elif row[j] == 2:
            sr, sc = i, j

que = deque([(sr, sc, 0)])

while que:
    cr, cc, cost = que.popleft()

    if dist[cr][cc] != -2:
        continue
    else:
        dist[cr][cc] = cost

    for r, c in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        nr, nc = cr + r, cc + c

        if nr >= n or nr < 0 or nc >= m or nc < 0:
            continue

        que.append((nr, nc, cost+1))

for i in range(n):
    for j in range(m):
        if dist[i][j] == -2:
            print(-1, end = " ")
        else:
            print(dist[i][j], end = " ")
    print()
