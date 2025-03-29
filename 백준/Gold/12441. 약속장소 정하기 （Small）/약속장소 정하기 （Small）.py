# 약속장소 정하기(small)
import sys
input = sys.stdin.readline
import heapq as hq

T = int(input())

for i in range(T):
    # 도시, 친구, 도로의 숫자
    N, P, M = map(int,input().split()) 
    start = [0] * (N+1) # 친구 시작 도시 
    speed = [0] * (N+1) # 친구 이동속도
    graph = [[] for _ in range(N+1)] # 도로 연결그래프
    visited = [1] * (N+1) # 비트마스킹으로 방문 확인
    total = [0] * (N+1)
    
    for j in range(P):
        X, V = map(int,input().split())
        start[j+1] = X
        speed[j+1] = V

    for j in range(M):
        roads = list(map(int,input().split()))

        dist = roads[0]
        links = roads[1]
    
        for k in range(links):
            n1 = roads[2+k]
            for m in range(k+1, links):
                n2 = roads[2+m]
                graph[n1].append((n2, dist*(m-k)))
                graph[n2].append((n1, dist*(m-k)))

    for j in range(1, P+1):
        que = []
        hq.heappush(que, (0, start[j]))
        cur_speed = speed[j]
        visits = 0
        
        while que and visits < N:
            dist, city = hq.heappop(que)
            
            if visited[city] & (1 << j):
                continue
            else:
                visited[city] |= (1 << j)
                total[city] = max(total[city], dist)
                visits += 1

            for n_city, n_dist in graph[city]:

                if visited[n_city] & (1 << j):
                    continue

                hq.heappush(que, (n_dist*cur_speed + dist, n_city))
            
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

            
        
    
