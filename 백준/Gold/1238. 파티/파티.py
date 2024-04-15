# 파티
import sys
input = sys.stdin.readline
import heapq

n, m, x = map(int,input().split())

graph = [[] for _ in range(n)]
for i in range(m):
    start, to, cost = map(int,input().split())
    heapq.heappush(graph[start-1], (cost, to-1))

total_cost = [0] * n

def dijkstra(start, to):
    que = graph[start].copy()
    visit = [0] * n
    visit[start] = -1
    
    while que:
        # print(que)
        cost, cur = heapq.heappop(que)

        visit[cur] = -1
        
        if cur == to:
            total_cost[i] += cost
            return
        
        for c, t in graph[cur]:
            if visit[t] == 0:
                heapq.heappush(que, (cost+c, t))
                
                

for i in range(n):
    if i == x-1:
        continue
    dijkstra(i, x-1)
    dijkstra(x-1, i)

print(max(total_cost))
