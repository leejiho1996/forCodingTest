# 미로 탐색
import sys
from collections import deque 
input = sys.stdin.readline

n, m = map(int,input().split())

maze = [list(input().rstrip()) for _ in range(n)]

que = deque([(0,0,1)])
maze[0][0] = '0'

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while que:
    row, col, cnt = que.popleft()

    if row == n-1 and col == m-1:
        print(cnt)
        break

    for r, c in move:
        next_row = row + r
        next_col = col + c
        if next_row == n-1 and next_col == m-1:
            print(cnt+1)
            que = deque([])
            break
        if 0 <= next_row < n and 0 <= next_col < m and maze[next_row][next_col] == '1':
            que.append((next_row, next_col, cnt+1))
            maze[next_row][next_col] = '0'
