# 구슬탈출2 bfs
import sys
input = sys.stdin.readline
from collections import deque

def move(r, c, dx, dy):
    cnt = 0

    while True:
        if graph[r][c] == "O":
            return [r, c, cnt]
        elif graph[r+dx][c+dy] == "#":
            return [r, c, cnt]
        
        r += dx
        c += dy
        cnt += 1
        
n, m = map(int,input().split())
result = 1000
graph = []
visited = [[[[0] * m for i in range(n)] for j in range(m)] for k in range(n)]

# 아래, 위, 오른쪽, 왼쪽 이동
direc = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for i in range(n):
    row = list(input().rstrip())
    graph.append(row)

    for j in range(m):
        if row[j] == "R":
            redR = i
            redC = j
        elif row[j] == "B":
            blueR = i
            blueC = j
        elif row[j] == "O":
            outR = i
            outC = j

que = deque([])
que.append((redR, redC, blueR, blueC, 0))

while que:
    rr, rc, br, bc, cnt = que.popleft()

    if cnt >= 10 or cnt > result:
        continue

    if visited[rr][rc][br][bc]:
        continue
    else:
        visited[rr][rc][br][bc] = 1

    for dx, dy in direc:
        nRed = move(rr, rc, dx, dy)
        nBlue = move(br, bc, dx, dy)

        if nBlue[0] == outR and nBlue[1] == outC:
            continue
        elif nRed[0] == outR and nRed[1] == outC:
            result = min(result, cnt+1)
            break

        if nRed[0] == nBlue[0] and nRed[1] == nBlue[1]:
            if nRed[2] < nBlue[2]:
                nBlue[0] -= dx
                nBlue[1] -= dy
            else:
                nRed[0] -= dx
                nRed[1] -= dy

        if not visited[nRed[0]][nRed[1]][nBlue[0]][nBlue[1]]:
            que.append((nRed[0], nRed[1], nBlue[0], nBlue[1], cnt+1))

if result == 1000:
    print(-1)
else:
    print(result)
        
