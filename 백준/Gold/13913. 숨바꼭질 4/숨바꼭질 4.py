# 숨바꼭질4
import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int,input().split())

que = deque()
que.append((n, 0))

visited = [0] * 100001
visited[n] = 1

route = [0] * 100001
route[n] = -1

while que:
    cur, sec = que.popleft()

    if cur == k:
        break

    for i in (cur-1, cur+1, cur*2):
        if 0 <= i <= 100000 and not visited[i]:
            que.append((i, sec+1))
            visited[i] = 1
            route[i] = cur

result = [k]

while route[k] != -1:
    k = route[k]
    result.append(k)

print(sec)
print(*result[::-1])
    
