# 템포럴 그래프
import sys
input = sys.stdin.readline

N, T, M = map(int,input().split())
S, E = map(int,input().split())
MAX = 10_000_001

# dp
dp = [MAX] * N
dp[S] = 0

for i in range(1, T+1):
    prev = dp.copy()
        
    for j in range(M):
        n1, n2, w = map(int,input().split())
        dp[n1] = min(dp[n1], prev[n2] + w)
        dp[n2] = min(dp[n2], prev[n1] + w)
        
if dp[E] == MAX:
    print(-1)
else:
    print(dp[E])
