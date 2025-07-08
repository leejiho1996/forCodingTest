from collections import deque
import sys
input = sys.stdin.readline

def bfs(i,j):
    
    cur = graph[i][j]
    maxx = 10
    que = deque([(i,j)])
    visits = [(i,j)]
    
    visited = [[0] * (M) for _ in range(N)]
    visited[i][j] = 1

    ret = 0
    
    while que:
        r, c = que.popleft()

        for dr, dc in direc:
            nr = r + dr
            nc = c + dc

            if nr < 0 or nc < 0 or nr >= N or nc >= M:
                return 0

            if visited[nr][nc]:
                continue

            if graph[nr][nc] > cur:
                maxx = min(maxx, graph[nr][nc])    
            else:
                que.append((nr, nc))
                visits.append((nr, nc))
                visited[nr][nc] = 1

    for r, c in visits:
        ret += maxx - graph[r][c] 
        graph[r][c] = maxx

    return ret

N, M = map(int, input().split())
graph = []
direc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
result = 0

for i in range(N):
    row = list(input().rstrip())
    graph.append(list(map(int, row)))
    
for i in range(1, N-1):
    for j in range(1, M-1):
        result += bfs(i,j)

print(result)
