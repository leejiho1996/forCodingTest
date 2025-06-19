# 총깡 총깡
import sys
input = sys.stdin.readline
import heapq as hq

N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]
LIMIT = 500001
visited = [LIMIT] * (N+1)

J = int(input())
K = int(input())
A = set(map(int,input().split()))
B = set(map(int,input().split()))

for i in range(M):
    s, t, c = map(int, input().split())

    graph[s].append((t, c))
    graph[t].append((s, c))

que = []

# 진서를 시작점으로 주변 도시를 힙큐에 담는다
for city, cost in graph[J]:
    hq.heappush(que, (cost, city))
    visited[city] = cost

minA = LIMIT
minB = LIMIT

# 모든 도시까지의 최단거리를 다익스트라로 탐색
while que:
    cost, city = hq.heappop(que)

    if visited[city] < cost:
        continue
    
    if city in A:
        minA = min(minA, cost)
    
    if city in B:
        minB = min(minB, cost)

    if minA != LIMIT and minB != LIMIT:
        break
    
    for ncity, ncost in graph[city]:
        if visited[ncity] <= cost + ncost:
            continue

        hq.heappush(que, (cost + ncost, ncity))
        visited[ncity] = cost + ncost

# 둘다 도달하지 못하면 -1 출력
if minA == LIMIT and minB == LIMIT:
    print(-1)
elif minA <= minB: # A, B 둘다 같은 경우 A를 출력
    print("A")
    print(minA)
else:
    print("B")
    print(minB)  
