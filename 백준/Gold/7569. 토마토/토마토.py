# 토마토(3d)
import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int,input().split())

que = deque([])
tomato = True
board = []
for k in range(h):
    temp = []
    for i in range(n):
        temp_b = list(map(int,input().split()))
        count = 0
        for j in temp_b:
            if j == 1:
                que.append((k, i, count))
            elif j == 0:
                tomato = False
            count += 1
        temp.append(temp_b)
    board.append(temp)
   
pos = [(0,-1,0), (0,1,0), (0,0,-1), (0,0,1), (1,0,0),(-1,0,0)]

def bfs():
    while que:
        height, row, col = que.popleft()

        for he, r, c in pos:
            new_height = height + he
            new_row = row + r
            new_col = col + c

            if 0 <= new_height < h and 0 <= new_row < n and 0 <= new_col < m and board[new_height][new_row][new_col] == 0:
                que.append((new_height, new_row, new_col))
                board[new_height][new_row][new_col] = board[height][row][col] + 1

maxx = 0
if tomato:
    print(0)
else:
    bfs()
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if board[k][i][j] == 0:
                    print(-1)
                    sys.exit()
                maxx = max(board[k][i][j], maxx)
    print(maxx-1)