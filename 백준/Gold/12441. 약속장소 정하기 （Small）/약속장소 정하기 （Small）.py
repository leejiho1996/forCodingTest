# 약속장소 정하기(small)
import sys
input = sys.stdin.readline
import heapq as hq

def dijkstra(n):
    que = []
    local_visited = [0] * (N+1)
    dist = [float('inf')] * (N+1)
    dist[start[n]] = 0    
    hq.heappush(que, (0, start[n]))
    cur_speed = speed[n]
    
    while que:
        cost, cur = hq.heappop(que)

        if local_visited[cur]:
            continue

        local_visited[cur] = 1
        visited[cur] |= (1 << n)
        total[cur] = max(total[cur], cost)

        # 최소거리가 갱신 가능한 경우만 que에 넣는다
        for ncity, ncost in graph[cur]:
            if dist[ncity] > cost + ncost*cur_speed:
                dist[ncity] = cost + ncost*cur_speed
                hq.heappush(que, (dist[ncity], ncity))

T = int(input())

for i in range(T):
    # 도시, 친구, 도로의 숫자
    N, P, M = map(int,input().split()) 
    start = [0] * (N+1) # 친구 시작 도시 
    speed = [0] * (N+1) # 친구 이동속도
    graph = [[] for _ in range(N+1)] # 도로 연결그래프
    visited = [1] * (N+1) # 비트마스킹으로 방문 확인
    total = [0] * (N+1) # 도시별 최대 도달시간 저장
    
    for j in range(P):
        X, V = map(int,input().split())
        start[j+1] = X
        speed[j+1] = V

    for j in range(M):
        roads = list(map(int,input().split()))

        dist = roads[0]
        links = roads[1]

        # 주어진 도로들의 연결정보 저장
        for k in range(links):
            n1 = roads[2+k]
            for m in range(k+1, links):
                n2 = roads[2+m]
                graph[n1].append((n2, dist*(m-k)))
                graph[n2].append((n1, dist*(m-k)))

    for j in range(1, P+1):
        dijkstra(j)
            
    minn = float('inf')
    for j in range(1, N+1):
        if visited[j] != (1 << (P+1)) - 1:
            continue

        if minn > total[j]:
            minn = total[j]

    if minn == float('inf'):
        print(f'Case #{i+1}: -1')
    else:
        print(f'Case #{i+1}: {minn}')
