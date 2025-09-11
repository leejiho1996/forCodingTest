# 내려가기2
import sys
input = sys.stdin.readline

N = int(input())
graph = []

for i in range(N):
    graph.append(list(map(int,input().split())))

min_dp = [[0] * 3 for _ in range(2)]
max_dp = [[0] * 3 for _ in range(2)]

min_dp[0] = graph[0].copy()
max_dp[0] = graph[0].copy()

prev = -1
cur = 0

for i in range(1, N):

    if i % 2:
        prev = 0
        cur = 1
    else:
        prev = 1
        cur = 0
        
    min_dp[cur][0] = graph[i][0] + min(min_dp[prev][0], min_dp[prev][1])
    min_dp[cur][1] = graph[i][1] + min(min_dp[prev][0], min_dp[prev][1], min_dp[prev][2])
    min_dp[cur][2] = graph[i][2] + min(min_dp[prev][1], min_dp[prev][2])

    max_dp[cur][0] = graph[i][0] + max(max_dp[prev][0], max_dp[prev][1])
    max_dp[cur][1] = graph[i][1] + max(max_dp[prev][0], max_dp[prev][1], max_dp[prev][2])
    max_dp[cur][2] = graph[i][2] + max(max_dp[prev][1], max_dp[prev][2])

print(max(max_dp[cur]), min(min_dp[cur]))
