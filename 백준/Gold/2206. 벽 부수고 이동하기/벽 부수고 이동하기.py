# 벽 부수고 이동하기
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())

board = [list(input().rstrip()) for _ in range(n)]

break_visit = [[float('inf')] * m for _ in range(n)] # 벽을 깨고 간 루트
visit = [[float('inf')] * m for _ in range(n)] # 그냥 간 루트

pos = [(-1,0), (1,0), (0,-1), (0,1)] # 상하좌우

que = deque([(0,0,False, 1)])
visit[0][0] = 1

while que:
    row, col, break_check, cnt = que.popleft()

    for r, c in pos:
        next_r = row + r
        next_c = col + c

        if 0 <= next_r < n and 0 <= next_c < m:
            if board[next_r][next_c] == '1' and break_check == False and break_visit[next_r][next_c] > cnt+1:
                que.append((next_r, next_c, True, cnt+1))
                break_visit[next_r][next_c] = cnt + 1

            if board[next_r][next_c] == '0':
                if not break_check and visit[next_r][next_c] > cnt+1:
                    que.append((next_r, next_c, break_check, cnt+1))
                    visit[next_r][next_c] = cnt + 1
                    

                elif break_check and break_visit[next_r][next_c] > cnt+1: 
                    que.append((next_r, next_c, break_check, cnt+1))
                    break_visit[next_r][next_c] = cnt+1
                    
if min(break_visit[n-1][m-1], visit[n-1][m-1]) == float('inf'):
    print(-1)
else:
    print(min(break_visit[n-1][m-1], visit[n-1][m-1]))
