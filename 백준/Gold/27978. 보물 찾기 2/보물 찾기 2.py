# 보물 찾기 2
import sys
input = sys.stdin.readline
import heapq as hq

H, W = map(int,input().split())
graph = []
visited = [[float('inf')] * W for _ in range(H)]
direc = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, -1), (1, 1), (-1, -1), (-1, 1)]

for i in range(H):
    row = list(input().rstrip())
    graph.append(row)

for i in range(H):
    for j in range(W):
        if graph[i][j] == 'K':
            sr = i
            sc = j
            break

visited[sr][sc] = 0

que = []
for dx, dy in direc:
    nr, nc = sr + dx, sc + dy

    if nr < 0 or nc < 0 or nr >= H or nc >= W:
        continue

    if graph[nr][nc] == '#':
        continue

    if dy == 1:
        hq.heappush(que, (0, nr, nc))
    else:
        hq.heappush(que, (1, nr, nc))

while que:
    cost, r, c = hq.heappop(que)

    if visited[r][c] <= cost:
        continue
    else:
        visited[r][c] = cost

    if graph[r][c] == '*':
        print(cost)
        exit()

    for dx, dy in direc:
        nr, nc = r + dx, c + dy

        if nr < 0 or nc < 0 or nr >= H or nc >= W:
            continue

        if graph[nr][nc] == "#":
            continue

        if dy == 1 and visited[nr][nc] > cost:
            hq.heappush(que, (cost, nr, nc))
        elif visited[nr][nc] > cost:
            hq.heappush(que, (cost+1, nr, nc))
        
print(-1)
