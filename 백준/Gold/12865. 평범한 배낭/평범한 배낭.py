# 평범한 배낭
import sys
input = sys.stdin.readline

n, k = map(int,input().split())

dp = [[0] * (k+1) for _ in range(n+1)]

weight = [0]
value = [0]

for i in range(n):
    w, v = map(int,input().split())
    weight.append(w)
    value.append(v)

for i in range(1, n+1):
    for j in range(1, k+1):
        if j - weight[i] >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]] + value[i])
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

print(dp[n][k])