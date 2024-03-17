# 숨바꼭질 3
import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int,input().split())
limit = 100_001

que = deque([n])
check = [-1] * limit
check[n] = 0
while que:
    position= que.popleft()

    if position == k:
        print(check[position])
        break

    for next_num in (position*2, position-1, position+1):
        if 0<= next_num < limit and check[next_num]==-1:
            if next_num == position*2:
                check[next_num] = check[position]
            else:
                check[next_num] = check[position] + 1

            que.append(next_num)