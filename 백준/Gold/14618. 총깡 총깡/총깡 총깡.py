# 총깡 총깡
import sys
input = sys.stdin.readline
import heapq as hq

N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited = [float('inf')] * (N+1)

J = int(input())
K = int(input())
A = set(map(int,input().split()))
B = set(map(int,input().split()))

for i in range(M):
    s, t, c = map(int, input().split())

    graph[s].append((t, c))
    graph[t].append((s, c))

que = []

for city, cost in graph[J]:
    hq.heappush(que, (cost, city))
    visited[city] = cost

minA = float('inf')
minB = float('inf')

while que:
    cost, city = hq.heappop(que)

    if visited[city] < cost:
        continue
    
    if city in A:
        minA = min(minA, cost)

    if city in B:
        minB = min(minB, cost)

    for ncity, ncost in graph[city]:
        if visited[ncity] <= cost + ncost:
            continue

        hq.heappush(que, (cost + ncost, ncity))
        visited[ncity] = cost + ncost

if minA == float('inf') and minB == float('inf'):
    print(-1)
elif minA <= minB:
    print("A")
    print(minA)
else:
    print("B")
    print(minB)  
