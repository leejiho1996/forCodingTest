# 유기농 배추
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

t = int(input())

def worm(x, y):
    if field[x][y] == 1:
        field[x][y] = "visited"
    else:
        return 0

    for i, j in [(-1,0), (1,0), (0,-1),(0,1)]:
        if 0 <= x+i < row and 0 <= y+j < col:
            worm(x+i, y+j)
    return 1

for i in range(t):
    col, row, vegi = map(int,input().split())
    field = [[0]*col for _ in range(row)]

    for j in range(vegi):
        x, y = map(int,input().split())
        field[y][x] = 1
    
    cnt = 0
    for k in range(row):
        for h in range(col):
            cnt += worm(k, h)
    print(cnt)