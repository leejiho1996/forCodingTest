# 쉬운 계단수
import sys
input = sys.stdin.readline

n = int(input())

cnt = 0

dp = [ [0]*10 for i in range(n)]

for i in range(1, 10):
    dp[0][i] = 1

for i in range(1, n):
    dp[i][9] = dp[i-1][8]
    dp[i][0] = dp[i-1][1]
    for j in range(1, 9):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

for i in range(10):
    cnt += dp[n-1][i]

print(cnt%1000000000)