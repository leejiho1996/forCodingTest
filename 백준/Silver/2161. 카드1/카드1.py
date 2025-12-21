# 카드 1
import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
que = deque([i for i in range(1, N+1)])
result = []

while que:
    result.append(que.popleft())

    if not que:
        break
    
    que.append(que.popleft())

print(*result)
