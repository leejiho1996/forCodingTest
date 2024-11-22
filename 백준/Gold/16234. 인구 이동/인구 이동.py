# 인구 이동
import sys
input = sys.stdin.readline
from collections import deque

n, L, R = map(int,input().split())
graph = []
direc = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for i in range(n):
    graph.append(list(map(int,input().split())))

def bfs(unions):
    elements = []
    total = 0
    
    while unions:
        r, c = unions.popleft()

        if visited[r][c]:
            continue

        visited[r][c] = 1
        elements.append((r,c))
        cur = graph[r][c]
        total += cur
        
        for x, y in direc:
            nr = r + x
            nc = c + y

            if not (0 <= nr < n) or not (0 <= nc < n):
                continue

            if visited[nr][nc]:
                continue
            
            diff = abs(cur - graph[nr][nc])

            if L <= diff <= R:
                unions.append((nr, nc))

    return (elements, total)

cnt = 0
while True:
    change = False
    visited = [[0] * n for _ in range(n)]
    group = []
    for i in range(n):
        for j in range(n):
            
            if visited[i][j]:
                continue
            
            cur = graph[i][j]
            for x, y in direc:
                ni = i + x
                nj = j + y

                if not (0 <= ni < n) or not (0 <= nj < n):
                    continue
                
                diff = abs(graph[ni][nj] - cur)
                
                if L <= diff <= R:
                    change = True
                    group.append(bfs(deque([(i, j)])))
                    break
                
    if not change:
        print(cnt)
        break
    else:
        cnt += 1

    for u, t in group:
        population = t // len(u)

        for r, c in u:
            graph[r][c] = population
            