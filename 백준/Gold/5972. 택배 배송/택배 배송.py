import sys
input = sys.stdin.readline
import heapq as hq

n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]
que = []

for i in range(m):
    start, to , cost = map(int,input().split())
    graph[start].append((to, cost))
    graph[to].append((start, cost))

visited = [0] * (n+1)
visited[1] = 1

for to, cost in graph[1]:
    hq.heappush(que, (cost, to)) 

while que:
    cost, to = hq.heappop(que)

    if visited[to]:
        continue

    if to == n:
        print(cost)
        break

    visited[to] = 1

    for nt, nc in graph[to]:
        if visited[nt]:
            continue
        
        hq.heappush(que, (cost+nc, nt))
