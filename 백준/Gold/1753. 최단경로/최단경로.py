# 최단 경로
import sys
import heapq
input = sys.stdin.readline

v, e = map(int,input().split())
k = int(input())

visit = [[] for _ in range(v+1)]

for _ in range(e):
    u, t, w = map(int,input().split())

    visit[u].append((w,t))

def dijkstra(start):
    que = []
    heapq.heappush(que, (0, start))

    distance = [sys.maxsize]*(v+1)
    distance[start] = 0
    
    while que:
        cur_weight, cur_node = heapq.heappop(que)

        if distance[cur_node] < cur_weight:
            continue
        
        for next_weight, next_node in visit[cur_node]:
            next_weight += cur_weight
            
            if distance[next_node] <= next_weight:
                continue
            
            distance[next_node] = next_weight
            heapq.heappush(que, (next_weight, next_node))
            
            
    return distance

distance = dijkstra(k)

for i in range(1,v+1):
    if distance[i] == sys.maxsize:
        print("INF")
    else:
        print(distance[i])
