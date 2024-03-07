# 동전 1
import sys
input = sys.stdin.readline

n, k = map(int,input().split())

coin = [int(input()) for _ in range(n)]

coin.sort()
dp = [0]*(k+1)

for i in coin:
    if i > k:
        continue
    dp[i] += 1
    for j in range(i+1, k+1):
        dp[j] = dp[j-i] + dp[j]
    
print(dp[k])
