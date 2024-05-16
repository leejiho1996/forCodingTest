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

    if cur-1 >= 0 and not visited[cur-1]:
        que.append((cur-1, sec+1))
        visited[cur-1] = 1
        route[cur-1] = cur
        
    if cur+1 <= 100000 and not visited[cur+1]:
        que.append((cur+1, sec+1))
        visited[cur+1] = 1
        route[cur+1] = cur
        
    if cur*2 <= 100000 and not visited[cur*2]:
        que.append((cur*2, sec+1))
        visited[cur*2] = 1
        route[cur*2] = cur

result = [k]

while route[k] != -1:
    k = route[k]
    result.append(k)

print(sec)
print(*result[::-1])
    
