# 토마토
import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]

pos = [(-1,0), (1,0), (0,-1), (0,1)]
target = m*n
que = deque([])

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            que.append((i,j,0))
        if board[i][j] == -1:
            target -= 1

cnt = len(que)

if cnt == target:
    print(0)
    exit()

while que:
    row, col, day = que.popleft()

    for r, c in pos:
        new_row = row + r
        new_col = col + c

        if 0 <= new_row < n and 0 <= new_col < m and board[new_row][new_col] == 0:
            que.append((new_row, new_col, day+1))
            cnt += 1
            board[new_row][new_col] = -1
            if cnt == target:
                print(day+1)
                exit()
    
print(-1)