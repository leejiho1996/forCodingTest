# 연구소
import sys
input = sys.stdin.readline

def nearWall(i, j):
    direc = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]

    for dx, dy in direc:
        nr, nc = i + dx, j + dy
        if nr < 0 or nr >= n or nc < 0 or nc >= m:
            return True
        elif graph[nr][nc] >= 1:
            return True

    return False

def getCount():
    visited = [[0] * m for _ in range(n)]
    safe = 0
    
    for i in range(n):
        for j in range(m):
            if visited[i][j] or graph[i][j] != 2:
                continue

            stack = [(i, j)]
            while stack:
                r, c = stack.pop()

                if visited[r][c]:
                    continue
                else:
                    visited[r][c] = 1
                    
                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nr, nc = r + dx, c + dy
                    if nr < 0 or nr >= n or nc < 0 or nc >= m:
                        continue
                    elif graph[nr][nc] == 1 or visited[nr][nc]:
                        continue
                    else:
                        stack.append((nr, nc))

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0 and not visited[i][j]:
                safe += 1

    return safe
            
def backtrack(limit, cnt):
    global result
    
    if cnt == 3:
        result = max(result, getCount())
        return

    for i in range(n):
        for j in range(m):
            if visited[i][j] or graph[i][j] != 0:
                continue
            elif limit >= i * n + j:
                continue
            elif not nearWall(i, j):
                continue
            else:
                visited[i][j] = 1
                graph[i][j] = 1
                backtrack(i * n + j, cnt+1)
                visited[i][j] = 0
                graph[i][j] = 0
    
n, m = map(int,input().split())
graph = []
visited = [[0] * m for _ in range(n)]
result = 0

for i in range(n):
    graph.append(list(map(int,input().split())))

backtrack(-1, 0)

print(result)

