# 숨바꼭질 
from collections import deque
import sys
input = sys.stdin.readline


a, b = map(int,input().split())
if a >= b :
    print(a - b)
    exit()
else:
    number = [True]*100001
    
def bfs(n, cnt):
    que = deque()
    que.append((n,cnt))

    while que:
        next_n, count = que.popleft()

        if next_n == b:
            print(count)
            break

        for i in (next_n+1, next_n-1, next_n*2):
            if 0<= i <= 100000 and number[i]:
                que.append((i, count+1))
                number[i] = False

bfs(a, 0)
