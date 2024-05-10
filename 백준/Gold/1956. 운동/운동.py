# 운동
import sys
input = sys.stdin.readline

v, e = map(int,input().split())

graph = [[float('inf')] * (v+1) for _ in range(v+1)]

for i in range(e):
    start, to, cost = map(int,input().split())
    graph[start][to] = cost

for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

result = float('inf')

for i in range(1, v+1):
    result = min(result, graph[i][i])

if result == float('inf'):
    print(-1)
else:
    print(result)
