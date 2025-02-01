# 치즈
import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10001)

def dfs(r, c):
    graph[r][c] = 3
    visited[r][c] = 1
    
    for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nr, nc = r + x, c + y

        if nr < 0 or nr >= n or nc < 0 or nc >= m:
            continue
        elif visited[nr][nc]:
            continue
        elif graph[nr][nc] == 0 or graph[nr][nc] == 3:
            dfs(nr, nc)


n, m = map(int, input().split())
graph = []
visited = [[0] * m for _ in range(n)]
time = 0

for i in range(n):
    row = list(map(int,input().split()))
    graph.append(row)
    
while True:
    visited = [[0] * m for _ in range(n)]
    melt = []
    dfs(0, 0)

    for r in range(n):
        for c in range(m):
            if graph[r][c] != 1:
                continue
            cnt = 0
            for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nr, nc = r + x, c + y
                if nr < 0 or nr >= n or nc < 0 or nc >= m:
                    continue

                if graph[nr][nc] == 3:
                    cnt += 1

            if cnt >= 2:
                melt.append((r, c))

    if not melt:
        break
    
    for r, c in melt:
        graph[r][c] = 3

    time += 1
    

print(time)
