# 백채원
import sys
input = sys.stdin.readline
from collections import deque

N, M, K = map(int,input().split())

graph = [[] for _ in range(N+1)]
dist = [float('inf')] * (N+1)
dist2 = [float('inf')] * (N+1)

for i in range(M):
    a, b, t = map(int,input().split())
    graph[a].append((b, t))
    graph[b].append((a, t))

que = deque([])

for i in list(map(int,input().split())):
    dist[i] = 0
    que.append((i, 0))
    
while que:
    cur, cost = que.popleft()

    for n, nc in graph[cur]:

        if dist[n] <= cost + nc:
            continue

        dist[n] = cost + nc
        que.append((n, nc + cost))

que = deque([])
que.append((1, 0))
dist2[1] = 0

result = []

while que:
    cur, cost = que.popleft()

    for n, nc in graph[cur]:

        if dist2[n] <= cost + nc:
            continue

        dist2[n] = cost + nc
        que.append((n, nc + cost))

for i in range(2, N+1):
    if dist[i] > dist2[i]:
        result.append(i)

if len(result) == 0:
    print(0)
else:
    print(*result)
