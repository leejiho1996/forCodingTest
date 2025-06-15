# 점프 숨바꼭질
import sys
input = sys.stdin.readline
from collections import deque

K = int(input())
dic = {}

que = deque([(0, 1, 0)])
dic[0] = 0
LIMIT = 10**12

while que:
    cur, jump, time = que.popleft()
    
    minus = cur - jump
    plus = cur + jump
    
    if minus not in dic and minus >= -LIMIT:
        dic[minus] = time + 1
        que.append((minus, jump * 2, time+1))
        
    if plus not in dic and plus <= LIMIT:
        dic[plus] = time + 1
        que.append((plus, jump * 2, time+1))

if K in dic:
    print(dic[K])
else:
    print(-1)
