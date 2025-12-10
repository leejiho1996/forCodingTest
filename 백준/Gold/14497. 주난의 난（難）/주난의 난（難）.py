# 주난의 난
import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    que = deque([])
    que.append((x1, y1))
    visited[x1][y1] = 1
    
    while que:
        x, y = que.popleft()
    
        for dx, dy in direc:
            nx, ny = x + dx, y + dy
            
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            if visited[nx][ny]:
                continue
            else:
                visited[nx][ny] = 1

            if graph[nx][ny] == '1':
                graph[nx][ny] = '0'
                continue

            if graph[nx][ny] == "#":
                return True
            
            que.append((nx, ny))

    return False
            
N, M = map(int,input().split())
graph = []
direc = [(1, 0), (-1, 0), (0, 1), (0, -1)]

x1, y1, x2, y2 = map(int,input().split())
x1 -= 1; y1 -=1

for i in range(N):
    row = list(input().rstrip())
    graph.append(row)

cnt = 0
while True:
    
    cnt += 1
    visited = [[0] * M for _ in range(N)]
    
    if bfs():
        break

print(cnt)

    
