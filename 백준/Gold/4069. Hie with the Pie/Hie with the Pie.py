# Hie with the Pie
import sys
input = sys.stdin.readline

def dfs(n, visited):

    if visited == (1 << (N+1)) - 1:
        return graph[n][0]

    if dp[n][visited] != -1:
        return dp[n][visited]
    else:
        dp[n][visited] = float('inf')

    for i in range(1, N+1):
        if visited & 1 << i:
            continue
        
        dp[n][visited] = min(dp[n][visited], graph[n][i] + dfs(i, visited | 1 << i))
    
    return dp[n][visited]
        
while True:
    N = int(input())

    if N == 0:
        break
    
    graph = []
    for i in range(N+1):
        graph.append(list(map(int,input().split())))

    # 플로이드 워셜로 각 노드별 최단거리 계산
    for k in range(N+1):
        for i in range(N+1):
            for j in range(N+1):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                
    dp = [[-1] * (1 << N+1) for _ in range(N+1)] 
    print(dfs(0,1))
