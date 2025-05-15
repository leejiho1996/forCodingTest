# 거의 최단 경로
import sys
input = sys.stdin.readline
import heapq as hq
from collections import deque

def dijkstra():
    que = []
    hq.heappush(que, (0, S, S))

    while que:
        cost, cur, prev = hq.heappop(que)

        if dist[cur] < cost:
            continue
        
        if dist[cur] == float('inf'):
            dist[cur] = cost
            route[prev][cur] = 1
        else:
            route[prev][cur] = 1
            continue

        for n, nc in graph[cur]:

            if dist[n] < nc + cost:
                continue
            elif banned[cur][n]:
                continue
            else:
                hq.heappush(que, (nc+cost, n, cur))

while True:
    N, M = map(int,input().split())
    if (N == 0 and M == 0):
        break

    S, D = map(int,input().split())
    dist = [float('inf')] * N
    route = [[0] * N for _ in range(N)]
    banned = [[0] * N for _ in range(N)]
    
    graph = [[] for _ in range(N)]
    for i in range(M):
        U, V, P  = map(int,input().split())
        graph[U].append((V, P))
    
    dijkstra()
    short = dist[D]

    deq = deque([D])
    while deq:
        cur = deq.popleft()
        
        for i in range(N):
            if i == cur:
                continue
            
            if route[i][cur] and banned[i][cur] == 0:
                banned[i][cur] = 1
                deq.append(i)

    dist = [float('inf')] * N
    dijkstra()

    if dist[D] == float('inf') or short == dist[D]:
        print(-1)
    else:
        print(dist[D])
