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

        # 이동한 루트 기록
        route[prev][cur] = 1
        
        if dist[cur] == float('inf'):
            # 처음 방문하는 거라면 거리 갱신후 다음 루트 탐색
            dist[cur] = cost
        else: # 아니라면 또 탐색할 필요없으니 continue    
            continue

        for n, nc in graph[cur]:
            # 거리가 갱신되지 않는다면 패스
            if dist[n] < nc + cost:
                continue
            # 최단거리에 포함되는 경로면 패스
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

    # D에서 부터 거꾸로 탐색하며 최단거리에 포함되는 도로 체
    deq = deque([D])
    while deq:
        cur = deq.popleft()
        
        for i in range(N):
            if route[i][cur] and banned[i][cur] == 0:
                banned[i][cur] = 1
                deq.append(i)

    dist = [float('inf')] * N
    dijkstra()

    if dist[D] == float('inf') or short == dist[D]:
        print(-1)
    else:
        print(dist[D])
