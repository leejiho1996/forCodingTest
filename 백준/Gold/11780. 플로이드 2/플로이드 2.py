# 플로이드2
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[float('inf')]*(n+1) for _ in range(n+1)]
route = [[[] for _ in range(n+1)] for __ in range(n+1)]

for i in range(n+1):
    graph[i][i] = 0
         
for i in range(m):
    start, to, cost = map(int,input().split())
    if graph[start][to] > cost:
        graph[start][to] = cost
        route[start][to] = [start, to]

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                 graph[i][j] = graph[i][k] + graph[k][j]
                 route[i][j] = route[i][k] + route[k][j][1:]

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == float('inf'):
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()
    
for i in range(1, n+1):
    for j in range(1, n+1):
        if len(route[i][j]) == 0:
            print(0)
        else:
            print(len(route[i][j]), end = ' ')
            print(*route[i][j])
