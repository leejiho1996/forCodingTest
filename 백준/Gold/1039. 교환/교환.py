# 교환
import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int,input().split())
visited = [0] * 1000001
N = str(N)
length = len(N)
twice = False

if length < 2:
    print(-1)
    exit()
    
for i in N:
    if N.count(i) > 1:
        twice= True
        break
    
que = deque([(N, 1)])
maxx = 0

while que:
    cur, cnt = que.popleft()
    
    if visited[int(cur)] > 0:
        continue
    else:
        visited[int(cur)] = cnt

    maxx = max(maxx, int(cur))
    cur = list(cur)
    
    if cnt >= K+1:
        continue
    
    for i in range(length):
        for j in range(i, length):
            cur[i], cur[j] = cur[j], cur[i]
            
            if cur[0] != "0" and visited[int("".join(cur))] == 0:
                que.append(("".join(cur), cnt+1))

            cur[i], cur[j] = cur[j], cur[i]
            
K -= (visited[maxx] - 1)

maxx = list(str(maxx))

if twice:
    K = 0

while K:
    maxx[-1], maxx[-2] = maxx[-2], maxx[-1]

    if maxx[0] == "0":
        break

    K -= 1

if K:
    print(-1)
else:
    print(*maxx, sep="")
