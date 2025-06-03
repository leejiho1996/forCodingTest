# 알고스팟
import sys
input = sys.stdin.readline
import heapq as hq

N, M = map(int,input().split())
graph = []
visited = [[10001] * N for _ in range(M)]
direc = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for i in range(M):
    graph.append(input().rstrip())

que = []
hq.heappush(que, (0, 0, 0))

while que:
    cost, r, c = hq.heappop(que)

    if r == M-1 and c == N-1:
        print(cost)
        break
    
    if visited[r][c] <= cost:
        continue
    else:
        visited[r][c] = cost

    for dx, dy in direc:
        nr, nc = r + dx, c + dy

        if nr < 0 or nr >= M or nc < 0 or nc >= N:
            continue
        elif visited[nr][nc] <= cost + int(graph[nr][nc]):
            continue

        hq.heappush(que, (cost+int(graph[nr][nc]), nr, nc))
    

