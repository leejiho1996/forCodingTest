# 아기 상어
import sys
input = sys.stdin.readline
from collections import deque
    
def find(i, j):
    visited = [[0] * n for _ in range(n)]
    que = deque([(i, j, 0)])
    direc = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    minDist = 10000
    row = 0
    col = 0
    
    while que:
        r, c, dis = que.popleft()

        if visited[r][c]:
            continue
        else:
            visited[r][c] = 1

        if graph[r][c] != 0 and graph[r][c] < sharkSize:
            if dis < minDist:
                minDist = dis
                row = r
                col = c
            elif dis == minDist:
                if r < row:
                    row = r
                    col = c
                elif r == row and c < col:
                    row = r
                    col = c
                
        for x, y in direc:
            nr, nc = r + x, c + y

            if nr < 0 or nr >= n or nc < 0 or nc >= n:
                continue
            elif visited[nr][nc] or graph[nr][nc] > sharkSize:
                continue
            else:
                que.append((nr, nc, dis+1))

    return (minDist, row, col)

n = int(input())
graph = []
sharkSize = 2
total = 0
cnt = 0

for i in range(n):
    row = list(map(int,input().split()))
    for j in range(n):
        if row[j] == 9:
            row[j] = 0
            shark = (i, j) 
    graph.append(row)

while True:
    dis, r, c = find(shark[0], shark[1])

    if dis == 10000:
        break

    total += dis
    graph[r][c] = 0
    shark = (r, c)
    cnt += 1

    if cnt == sharkSize:
        cnt = 0
        sharkSize += 1
    
print(total)
