# 미세먼지 안녕!
import sys
input = sys.stdin.readline

r, c, t = map(int,input().split())
graph = []
move = []

for i in range(r):
    row = list(map(int,input().split()))
    graph.append(row)
    for j in range(c):
        if row[j] == -1:
            puri2 = i
    
puri1 = puri2-1

row = puri1 - 1
col = 0
dx = -1
dy = 0
while True:
    if row == puri1 and col == 0:
        break

    move.append((row, col, row+dx, col+dy))
    row += dx
    col += dy

    if row == 0 and col == 0:
        dx = 0
        dy = 1
    elif row == 0 and col == c-1:
        dx = 1
        dy = 0
    elif row == puri1 and col == c-1:
        dx = 0
        dy = -1

row = puri2 + 1
col = 0
dx = 1
dy = 0
while True:
    if row == puri2 and col == 0:
        break

    move.append((row, col, row+dx, col+dy))
    row += dx
    col += dy

    if row == r-1 and col == 0:
        dx = 0
        dy = 1
    elif row == r-1 and col == c-1:
        dx = -1
        dy = 0
    elif row == puri2 and col == c-1:
        dx = 0
        dy = -1

while t:
    newGraph = [[0] * c for _ in range(r)]
    
    for i in range(r):
        for j in range(c):
            if graph[i][j] <= 0:
                continue

            newGraph[i][j] += graph[i][j]
            
            for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = i + x, j + y
                
                if nr < 0 or nr >= r or nc < 0 or nc >= c:
                    continue
                elif (nr == puri1 and nc == 0) or (nr == puri2 and nc == 0):
                    continue
                else:
                    newGraph[nr][nc] += graph[i][j] // 5
                    newGraph[i][j] -= graph[i][j] // 5

    graph = newGraph

    for x, y, nx, ny in move:
        if (nx == puri1 and ny == 0) or (nx == puri2 and ny == 0):
            graph[x][y] = 0
        else:    
            graph[x][y] = graph[nx][ny]

    t -= 1

total = 0
for i in range(r):
    for j in range(c):
        total += graph[i][j]

print(total)
                    

