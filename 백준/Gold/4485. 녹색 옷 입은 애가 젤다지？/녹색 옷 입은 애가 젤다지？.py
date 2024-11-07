# 녹색 옷 입은 애가 젤다지?
import sys
input = sys.stdin.readline
from collections import deque

direc = [(0, 1), (1, 0), (0, -1), (-1, 0)]
p = 0
while True:
    n = int(input())

    if n == 0:
        break
    p += 1
    graph = []

    for i in range(n):
        graph.append(list(map(int,input().split())))

    visited = [[float('inf')] * n for _ in range(n)]

    que = deque([(0, 0, graph[0][0])])

    while que:
        cr, cc, cnt = que.popleft()

        if visited[cr][cc] < cnt:
            continue
        
        for r, c in direc:
            nr = cr + r
            nc = cc + c

            if not (0 <= nr < n) or not (0 <= nc < n):
                continue

            if graph[nr][nc] + cnt >= visited[nr][nc]:
                continue
        
            visited[nr][nc] = cnt + graph[nr][nc]
            que.append((nr, nc, cnt + graph[nr][nc]))
                
    print(f'Problem {p}: {visited[n-1][n-1]}')
        