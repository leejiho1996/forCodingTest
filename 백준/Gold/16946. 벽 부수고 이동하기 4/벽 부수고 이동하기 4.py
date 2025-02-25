# 벽 부수고 이동하기 4
import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int,input().split())
graph = []
visited = [[0] * m for _ in range(n)]
group = []
direc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
cnt = 1

for i in range(n):
    row = list(input().rstrip())
    graph.append(row)

for i in range(n):
    for j in range(m):
        if visited[i][j]:
            continue
        
        if graph[i][j] == '0':
            que = deque([])
            que.append((i, j))
            total = 0

            while que:
                r, c = que.popleft()

                if visited[r][c] != 0:
                    continue
                else:
                    visited[r][c] = cnt
                    total += 1

                for dx, dy in direc:
                    nr, nc = r + dx, c + dy

                    if nr < 0 or nc < 0 or nr >= n or nc >= m:
                        continue
                    elif visited[nr][nc] or graph[nr][nc] == "1":
                        continue
                    else:
                        que.append((nr, nc))

            group.append((cnt, total))
            cnt += 1

for i in range(n):
    for j in range(m):
        if graph[i][j] != '1':
            continue

        sett = set()
        possible = 1
        for dx, dy in direc:
            nr, nc = i + dx, j + dy

            if nr < 0 or nc < 0 or nr >= n or nc >= m:
                continue
            elif visited[nr][nc] in sett or visited[nr][nc] == 0:
                continue
            else:
                possible += group[visited[nr][nc]-1][1]
                sett.add(visited[nr][nc])
        
        graph[i][j] = str(possible%10)

for i in graph:
    print(*i, sep="")
