# 보물 찾기 2
import sys
input = sys.stdin.readline
from collections import deque

H, W = map(int,input().split())
graph = []
visited = [[float('inf')] * W for _ in range(H)]
direc = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, -1), (1, 1), (-1, -1), (-1, 1)]

for i in range(H):
    row = list(input().rstrip())
    graph.append(row)

for i in range(H):
    for j in range(W):
        if graph[i][j] == 'K':
            sr = i
            sc = j
            break

visited[sr][sc] = 0

que = deque([])
que.append((0, sr, sc))

while que:
    cost, r, c = que.popleft()

    if graph[r][c] == '*':
        print(cost)
        exit()

    for dx, dy in direc:
        nr, nc = r + dx, c + dy

        if nr < 0 or nc < 0 or nr >= H or nc >= W:
            continue

        if graph[nr][nc] == "#":
            continue

        if dy == 1 and visited[nr][nc] > cost:
            que.appendleft((cost, nr, nc))
            visited[nr][nc] = cost
        elif visited[nr][nc] > cost + 1:
            que.append((cost+1, nr, nc))
            visited[nr][nc] = cost+1
        
print(-1)
