# 산봉우리
import sys
input = sys.stdin.readline

def dfs(x, y, h):

    ret = True
    visited[x][y] = 1

    for dx, dy in direc:
        nx, ny = x + dx, y + dy

        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue
    
        if graph[nx][ny] == h and not visited[nx][ny]:
            ret &= dfs(nx, ny, h)
            
        elif graph[nx][ny] > h:
            ret = False

    return ret

N, M = map(int,input().split())
visited = [[0] * M for _ in range(N)]
cnt = 0
direc = [(1, 0), (-1, 0), (0, 1), (0, -1),
         (1, 1), (1, -1), (-1, 1), (-1, -1)]

graph = []
for i in range(N):
    graph.append(list(map(int,input().split())))

for i in range(N):
    for j in range(M):
        
        if visited[i][j]:
            continue

        if dfs(i, j, graph[i][j]):
            cnt += 1

print(cnt)
