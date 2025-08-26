# 배달
import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int,input().split())
graph = [[0] * M for _ in range(N)]
dic = {}
direc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visited = [[[[0] * M for _ in range(N)] for _ in range(4)] for _ in range(4)]

cnt = 1
for i in range(N):
    cur = input().rstrip()
    for j in range(M):
        graph[i][j] = cur[j]

        if graph[i][j] == "S":
            sr = i
            sc = j

        if graph[i][j] == "C":
            dic[(i,j)] = cnt
            cnt += 1

que = deque([])
que.append((sr, sc, 0, -1, 0))

while que:
    r, c, cnt, p, g  = que.popleft()

    if g == 3:
        print(cnt)
        exit()
        
    for d in range(4):
        dr, dc = direc[d]
        nr, nc = r + dr, c + dc

        if nr < 0 or nc < 0 or nr >= N or nc >= M:
            continue

        if graph[nr][nc] == "#":
            continue

        if visited[g][d][nr][nc]:
            continue

        if d == p:
            continue

        if graph[nr][nc] == "C":
            ng = g | dic[(nr, nc)]
        else:
            ng = g
            
        que.append((nr, nc, cnt+1, d, ng))
        visited[g][d][nr][nc] = 1
        
print(-1)


