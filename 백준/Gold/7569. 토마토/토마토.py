# 토마토(3d)
import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int,input().split())

board = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]

pos = [(0,-1,0), (0,1,0), (0,0,-1), (0,0,1), (1,0,0),(-1,0,0)]

target = m*n*h
que = deque([])

for k in range(h):
    for i in range(n):
        for j in range(m):
            if board[k][i][j] == 1:
                que.append((k,i,j,0))
            if board[k][i][j] == -1:
                target -= 1

cnt = len(que)

if cnt == target:
    print(0)
    exit()

while que:
    height, row, col, day = que.popleft()

    for he, r, c in pos:
        new_height = height + he
        new_row = row + r
        new_col = col + c

        if 0 <= new_height < h and 0 <= new_row < n and 0 <= new_col < m and board[new_height][new_row][new_col] == 0:
            que.append((new_height, new_row, new_col, day+1))
            cnt += 1
            board[new_height][new_row][new_col] = -1
            if cnt == target:
                print(day+1)
                exit()
    
print(-1)