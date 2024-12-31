# 적록색약
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100001)

def dfs(r, c, check):
    if check:
        visit = colorVisited
    else:
        visit = visited
        
    visit[r][c] = 1
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for x, y in direction:
        nx, ny = r + x, c + y
        if nx >= n or nx < 0 or ny >= n or ny < 0:
            continue
        elif visit[nx][ny]:
            continue
        elif graph[r][c] == graph[nx][ny]:
            dfs(nx, ny, check)

        # 색약인경우    
        if check:
            if (graph[r][c] == "R" or graph[r][c] == "G") and (graph[nx][ny] == "R" or graph[nx][ny] == "G"):
                dfs(nx, ny, check)
        
n = int(input())
graph = []
normal = 0 # 일반
color = 0 # 적록색약
visited = [[0] * n for _ in range(n)]
colorVisited = [[0] * n for _ in range(n)]

for i in range(n):
    graph.append(input().rstrip())

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j, 0)
            normal += 1
        if not colorVisited[i][j]:
            dfs(i, j, 1)
            color += 1

print(normal, color)
