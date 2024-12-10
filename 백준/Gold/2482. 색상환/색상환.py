# 색 상환
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10001)

n = int(input())
k = int(input())
dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(n+1):
    dp[i][0] = 1
    dp[i][1] = i

for i in range(3, n+1):
    for j in range(2, (i+1)//2 + 1):
        dp[i][j] = (dp[i-1][j] + dp[i-2][j-1]) % 1000000003

print((dp[n-3][k-1] + dp[n-1][k]) % 1000000003)
