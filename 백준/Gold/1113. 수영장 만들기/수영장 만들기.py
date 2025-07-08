import sys
from collections import deque
input = sys.stdin.readline

def bfs(r, c, height):

    visited[r][c] = 1
    que = deque([(r, c)])
    check = True
    ret = 0
    
    while que:
        r, c = que.popleft()
        ret += height - graph[r][c]
        graph[r][c] = height

        for dr, dc in direc:
            nr, nc = r + dr, c + dc

            if nr < 0 or nc < 0 or nr >= N or nc >= M:
                check = False
                continue

            if visited[nr][nc]:
                continue

            if graph[nr][nc] < height:
                que.append((nr, nc))
                visited[nr][nc] = True
    
    if check:
        return ret
    else:
        return 0

N, M = map(int, input().split())
graph = []
direc = [(-1, 0), (1, 0), (0, -1), (0, 1)]
result = 0

for i in range(N):
    row = list(input().rstrip())
    graph.append(list(map(int, row)))
    
for k in range(2, 10):
    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if visited[i][j]:
                continue
            
            if graph[i][j] < k:
                result += bfs(i, j, k)

print(result)
