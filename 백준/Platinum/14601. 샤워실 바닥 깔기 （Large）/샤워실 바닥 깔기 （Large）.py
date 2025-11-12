# 샤워실 바닥 깔기
import sys
input = sys.stdin.readline

def divide(k, x1, x2, y1, y2, sx, sy):
    global tile

    if k == 0:
        return
    
    check = False
    for i in range(x1-1, x2):
        for j in range(y1-1, y2):
            if graph[i][j] <= -1:
                check = True
                continue

            if k == 1 and graph[i][j] == 0:
                graph[i][j] = tile

    if k == 1:
        tile += 1

    if not check:
        graph[sx][sy] = -2
    
    x_mid = (x1 + x2) // 2
    y_mid =(y1 + y2) // 2
    
    divide(k-1, x1, x_mid, y1, y_mid, x_mid-1, y_mid-1)
    divide(k-1, x_mid+1, x2, y1, y_mid, x_mid, y_mid-1)

    divide(k-1, x1, x_mid, y_mid+1, y2, x_mid-1, y_mid)
    divide(k-1, x_mid+1, x2, y_mid+1, y2, x_mid, y_mid)

def change(x, y):
    graph[x][y] = tile 
    
    for dx, dy in direc:
        nx, ny = x + dx, y+ dy

        if nx < 0 or ny < 0 or nx >= L or ny >= L:
            continue

        if graph[nx][ny] != -2:
            continue

        change(nx, ny)
        
K = int(input())
hx, hy = map(int,input().split())

L = 1 << K

graph = [[0] * L for _ in range(L)]
graph[L-hy][hx-1] = -1

tile = 1
direc = [(1, 0), (-1, 0), (0, 1), (0, -1)]

divide(K, 1, L, 1, L, -1, -1)

for i in range(L):
    for j in range(L):
        if graph[i][j] == -2:
            change(i, j)
            tile += 1

for i in graph:
    print(*i)
