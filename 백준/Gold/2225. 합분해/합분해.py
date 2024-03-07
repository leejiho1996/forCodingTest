# 합분해
import sys
input = sys.stdin.readline

n, k = map(int,input().split())

dp = [1] * (n+1)

for i in range(2, k+1):
    for j in range(1, n+1):
        dp[j] = dp[j] + dp[j-1]
        
print(dp[n]%1000000000)