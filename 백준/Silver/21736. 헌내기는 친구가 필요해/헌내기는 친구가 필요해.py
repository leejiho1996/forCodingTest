# 헌내기는 친구가 필요해
import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int,input().split())
graph = []
visited = [[0] * m for _ in range(n)]
meets = 0 # 사람을 만난 횟수 

for i in range(n):
    row = input().rstrip()
    graph.append(row)
    for j in range(m):
        if row[j] == "I":
            doyeon = (i, j) # 도연이의 시작 위치

que = deque([doyeon])

while que:
    cr, cc = que.popleft()

    if visited[cr][cc]:
        continue
    else:
        visited[cr][cc] = 1

    if graph[cr][cc] == "P":
        meets += 1

    for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nr, nc = cr + x, cc + y

        if (0 > nr or nr >= n or 0 > nc or nc >= m):
            continue
        elif visited[nr][nc]:
            continue
        elif graph[nr][nc] == "X":
            continue

        que.append((nr, nc))

if meets:
    print(meets)
else:
    print("TT")
