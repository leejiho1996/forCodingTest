# Hie with the Pie
import sys
input = sys.stdin.readline

def dfs(n, total, cnt):
    global result
    
    if cnt == N:
        result = min(result, total + graph[n][0])
    
    for i in range(1, N+1):
        if visited[i]:
            continue

        visited[i] = 1
        dfs(i, total + graph[n][i], cnt+1)
        visited[i] = 0

while True:
    N = int(input())

    if N == 0:
        break
    
    graph = []
    for i in range(N+1):
        graph.append(list(map(int,input().split())))

    for k in range(N+1):
        for i in range(N+1):
            for j in range(N+1):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                
    result = float('inf')
    visited = [0] * (N+1)
    visited[0] = 1
    
    dfs(0, 0, 0)

    print(result)
