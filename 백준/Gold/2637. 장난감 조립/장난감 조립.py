# 장난감 조립
import sys
input = sys.stdin.readline

def dfs(n):

    if isMiddle[n] == 0:
        ret = [0] * (N+1)
        ret[n] = 1
        return ret
    
    if visited[n]:
        return dp[n]

    for i, cnt in graph[n]:
        result = dfs(i)
        for j in range(N):
            dp[n][j] += result[j] * cnt

        visited[i] = 1

    return dp[n]
        
N = int(input())
M = int(input())
isMiddle = [0] * (N+1)
visited = [0] * (N+1)
graph = [[] for _ in range(N+1)]
dp = [[0] * (N+1) for _ in range(N+1)]

for i in range(M):
    parts, need, cnt = map(int,input().split())
    graph[parts].append((need, cnt))
    isMiddle[parts] = 1

dfs(N)

for i in range(1, N+1):
    if isMiddle[i] == 0:
        print(i, dp[N][i])
