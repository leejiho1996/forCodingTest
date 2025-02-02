# 아기 상어
import sys
input = sys.stdin.readline
import heapq as hq
from collections import deque
    
def find(i, j):
    visited = [[0] * n for _ in range(n)]
    que = deque([(i, j, 0)])
    heap = []
    direc = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    while que:
        r, c, dis = que.popleft()

        if visited[r][c]:
            continue
        else:
            visited[r][c] = 1

        if graph[r][c] != 0 and graph[r][c] < sharkSize:
            hq.heappush(heap, (dis, r, c))
        
        for x, y in direc:
            nr, nc = r + x, c + y

            if nr < 0 or nr >= n or nc < 0 or nc >= n:
                continue
            elif visited[nr][nc] or graph[nr][nc] > sharkSize:
                continue
            else:
                que.append((nr, nc, dis+1))

    return heap

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
    heap = find(shark[0], shark[1])

    if not heap:
        break

    dis, r, c = hq.heappop(heap)
    total += dis
    graph[r][c] = 0
    shark = (r, c)
    cnt += 1

    if cnt == sharkSize:
        cnt = 0
        sharkSize += 1
    
print(total)
