# 내려가기2
import sys
input = sys.stdin.readline

N = int(input())
min_dp = [[0] * 3 for _ in range(2)]
max_dp = [[0] * 3 for _ in range(2)]
prev = -1
cur = 0

for i in range(N):
    row = list(map(int,input().split()))

    if i == 0:
        min_dp[0] = row.copy()
        max_dp[0] = row.copy()
        continue

    if i % 2:
        prev = 0
        cur = 1
    else:
        prev = 1
        cur = 0

    min_dp[cur][0] = row[0] + min(min_dp[prev][0], min_dp[prev][1])
    min_dp[cur][1] = row[1] + min(min_dp[prev][0], min_dp[prev][1], min_dp[prev][2])
    min_dp[cur][2] = row[2] + min(min_dp[prev][1], min_dp[prev][2])

    max_dp[cur][0] = row[0] + max(max_dp[prev][0], max_dp[prev][1])
    max_dp[cur][1] = row[1] + max(max_dp[prev][0], max_dp[prev][1], max_dp[prev][2])
    max_dp[cur][2] = row[2] + max(max_dp[prev][1], max_dp[prev][2])

print(max(max_dp[cur]), min(min_dp[cur]))
