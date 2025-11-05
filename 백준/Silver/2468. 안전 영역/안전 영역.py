# 안전 영역
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100001)

def dfs(x, y, depth):

    visited[x][y] = 1

    for dx, dy in direc:
        nx, ny = x + dx, y + dy

        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue

        if visited[nx][ny] or graph[nx][ny] <= depth:
            continue

        dfs(nx, ny, depth)
    

N = int(input())
graph = []
result = 0
direc = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for i in range(N):
    graph.append(list(map(int,input().split())))

for d in range(101):
    cnt = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] or graph[i][j] <= d:
                continue
            else:
                cnt += 1
                dfs(i, j, d)

    result = max(result, cnt)

print(result)
