# 창영이의 퇴근
import sys
input = sys.stdin.readline
import heapq as hq

N = int(input())
graph = []
visited =[[0] * N for _ in range(N)]
direc = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for i in range(N):
    graph.append(list(map(int,input().split())))

que = []
hq.heappush(que, (0, 0, 0))

while que:
    cost, r, c = hq.heappop(que)

    if r == N-1 and c == N-1:
        print(cost)
        break
    
    if visited[r][c]:
        continue
    else:
        visited[r][c] = 1

    for dx, dy in direc:
        nr, nc = r + dx, c + dy

        if nr < 0 or nc < 0 or nr >= N or nc >= N:
            continue
        elif visited[nr][nc]:
            continue
        
        incline = max(cost, abs(graph[r][c] - graph[nr][nc]))
        hq.heappush(que, (incline, nr, nc))

