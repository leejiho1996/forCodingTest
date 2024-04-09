# 뱀과 사다리 게임
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())

board = [[i, i] for i in range(101)]

for i in range(n+m):
    start, to = map(int,input().split())
    board[start][1] = to

que = deque([(1,0)])

def bfs():
    while que:
        start, cnt = que.popleft()
        for i in range(1, 7):
            nex = start + i
                
            if  board[nex][0] != board[nex][1]:
                nex = board[nex][1]
            if board[nex][0] == -1:
                continue
            if nex == 100:
                print(cnt+1)
                return
            
            que.append((nex, cnt+1))
            board[nex][0] = -1

bfs()
