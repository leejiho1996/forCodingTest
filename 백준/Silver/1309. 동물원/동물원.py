# 동물원
import sys
input =sys.stdin.readline

n = int(input())

dp = [0] * (n+1)

dp[0] = 3
dp[1] = 7

for i in range(2, n):
    dp[i] = (dp[i-1]*2 + dp[i-2]) % 9901

print(dp[n-1]%9901)