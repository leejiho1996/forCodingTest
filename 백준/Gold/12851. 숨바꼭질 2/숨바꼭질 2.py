# 숨바꼭질2
import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int,input().split())
shortest = 100000
cnt = 0
visited = [100001] * 100001

if n >= m:
    print(n - m)
    print(1)
    exit()

que = deque([])
que.append((n, 0))

while que:
    cur, time = que.popleft()

    if time > shortest:
        break
    
    if cur == m:
        shortest = time
        cnt += 1
        continue

    if visited[cur] < time:
        continue
    else:
        visited[cur] = time

    for v in [cur-1, cur+1, cur*2]:
        if 0 <= v <= 100000 and visited[v] >= time+1:
            que.append((v, time+1))

print(shortest)
print(cnt)
