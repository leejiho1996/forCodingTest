# 미확인 도착지
import sys
input = sys.stdin.readline
import heapq

def dijkstra(s):
    que = [(0, s)]
    visited = [float('inf')] * (n+1)
    visited[s] = 0
    
    while que:
        cost, to = heapq.heappop(que)

        if visited[to] < cost:
            continue
            
        for i in graph[to]:
            next_cost, next_to = i
    
            if next_cost + cost < visited[next_to]:
                heapq.heappush(que, (cost+next_cost, next_to))
                visited[next_to] = cost+next_cost

    return visited
            
T = int(input())

for i in range(T):
    result = []
    
    n, m, t = map(int,input().split())
    s, g, h = map(int,input().split())

    graph = [[] for _ in range(n+1)]
    
    for j in range(m):
        a, b, d = map(int,input().split())
        if (a,b) == (g,h) or (a,b) == (h,g):
            graph[a].append((d*2-1, b))
            graph[b].append((d*2-1, a))
            continue
        
        graph[a].append((d*2,b))
        graph[b].append((d*2,a))

    possible = []
    
    for j in range(t):
        possible.append(int(input()))

    r = dijkstra(s)

    for i in sorted(possible):
        if r[i] % 2 == 1:
            print(i, end = ' ')