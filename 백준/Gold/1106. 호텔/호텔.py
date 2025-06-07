# 호텔
import sys
input = sys.stdin.readline

C, N = map(int,input().split())
info = []

for i in range(N):
    c, g = map(int,input().split())
    info.append((c, g))
    
dp = [1000000] * (C+1)
dp[0] = 0

for cost, get in info:
    for j in range(get, C+get+1):
        if j >= C:
            dp[C] = min(dp[C], dp[j-get] + cost)
        else:
            dp[j] = min(dp[j], dp[j - get] + cost)

print(dp[C])
