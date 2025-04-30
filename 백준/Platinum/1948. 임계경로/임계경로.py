# 임계경로
import sys
input = sys.stdin.readline
import heapq
from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
r_graph = [[] for _ in range(n+1)]  
dist = [0] * (n+1)

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    r_graph[v].append((u, w))  

start, end = map(int, input().split())

hq = []
heapq.heappush(hq, (-0, start))  
while hq:
    cost, now = heapq.heappop(hq)
    cost = -cost
    if dist[now] > cost:
        continue
    for to, weight in graph[now]:
        if dist[to] < dist[now] + weight:
            dist[to] = dist[now] + weight
            heapq.heappush(hq, (-(dist[to]), to))  

visited = [0] * (n+1)
count = 0
q = deque([end])
while q:
    cur = q.popleft()
    for prev, weight in r_graph[cur]:
        if dist[prev] + weight == dist[cur]:
            count += 1
            if not visited[prev]:
                visited[prev] = 1
                q.append(prev)

print(dist[end]) 
print(count)      
