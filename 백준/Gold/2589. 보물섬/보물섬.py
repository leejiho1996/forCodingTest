# 보물섬
import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int,input().split())
graph = []
direc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
maxx = 0

for i in range(N):
    row = list(input().rstrip())
    graph.append(row)

for i in range(N):
    for j in range(M):
        if graph[i][j] != "L":
            continue
        
        visited = [[0]*M for _ in range(N)]
        que = deque([(i, j, 0)])

        while que:
            r, c, cnt= que.popleft()

            if visited[r][c]:
                continue
            else:
                visited[r][c] = 1
                maxx = max(maxx, cnt)

            for dx, dy in direc:
                nr, nc = r + dx, c + dy

                if nr < 0 or nc < 0 or nr >= N or nc >= M:
                    continue
                elif graph[nr][nc] == "W":
                    continue
                else:
                    que.append((nr, nc, cnt+1))

print(maxx)
        
