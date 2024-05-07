# 플로이드 (플로이드 방법)
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[float('inf')]*(n+1) for _ in range(n+1)]

for i in range(m):
    start, to , cost = map(int,input().split())

    if graph[start][to] > cost:
        graph[start][to] = cost

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
    
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == float('inf') or i == j:
            print(0, end= ' ')
        else:
            print(graph[i][j], end=' ')
    print()