# 1, 2, 3 더하기 4
import sys
input = sys.stdin.readline

dp = [[0]*4 for _ in  range(10001)]

dp[1][1] = 1

dp[2][1] = 1
dp[2][2] = 1

dp[3][1] = 1
dp[3][2] = 1
dp[3][3] = 1

for i in range(4, 10001):
    dp[i][1] = dp[i-1][1]
    dp[i][2] = dp[i-2][1] + dp[i-2][2]
    dp[i][3] = dp[i-3][1] + dp[i-3][2] + dp[i-3][3]
    
t = int(input())

for i in range(t):
    n = int(input())
    print(dp[n][1] + dp[n][2] + dp[n][3])
    
