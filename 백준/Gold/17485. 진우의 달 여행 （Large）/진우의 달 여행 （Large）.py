# 진우의 달 여행
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
result = float('inf')


graph = []
for i in range(N):
    graph.append(list(map(int,input().split())))

dp = [[[0] * 3 for _ in range(M)] for _ in range(N)]

for i in range(M):
    for j in range(3):
        dp[0][i][j] = graph[0][i]

for i in range(1, N):
    for j in range(M):
        dp[i][j][0] = graph[i][j] + min(dp[i-1][j][1], dp[i-1][j][2])

        if j == 0:
            dp[i][j][1] = float('inf')
        else:
            dp[i][j][1] = graph[i][j] + min(dp[i-1][j-1][0], dp[i-1][j-1][2])

        if j == M-1:
            dp[i][j][2] = float('inf')
        else:
            dp[i][j][2] = graph[i][j] + min(dp[i-1][j+1][0], dp[i-1][j+1][1])

for i in range(M):
    for j in range(3):
        result = min(result, dp[N-1][i][j])

print(result)
