# 특정한 최단 경로
import sys
import heapq
input = sys.stdin.readline

n, m = map(int,input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b, c = map(int,input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

v1, v2 = map(int,input().split())

def dijkstra(start, target):
    if start == target:
        return 0
    que = []
    
    for i in graph[start]:
        heapq.heappush(que, i)
        
    visited = [0] * (n+1)
    visited[start] = 1
            
    while que:
    
        cost, to = heapq.heappop(que)
        
        if to == target:
            return cost
    
        visited[to] = 1
        
        for co, nex in graph[to]:
            next_node = nex
            next_cost = cost+co
            
            if not visited[next_node]:
                heapq.heappush(que, (next_cost, next_node))
    
    return float('inf')

v1_first = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
v2_first = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)

cost = min(v1_first, v2_first)

if cost == float('inf'):
    print(-1)
else:
    print(cost)
