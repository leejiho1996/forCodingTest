# 나이트의 이동
import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

# 가능한 8방위
pos = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]


def bfs(start_row, start_col, cnt):
    que = deque([(start_row, start_col, cnt)])

    while que:
        cur_row, cur_col, cnt = que.popleft()
        
        if cur_row == t_r and cur_col == t_c:
            print(cnt)
            return

        for r, c in pos:
            next_row = cur_row + r
            next_col = cur_col + c
            if 0 <= next_row < size and 0 <= next_col < size and visit[next_col][next_row]:
                que.append((next_row, next_col, cnt+1))
                visit[next_col][next_row] = 0
        
        
for i in range(n):
    size = int(input())
    visit = [[1] * size for _ in range(size)]
    
    s_r, s_c = map(int,input().split())
    t_r, t_c = map(int,input().split())

    bfs(s_r, s_c, 0)
    