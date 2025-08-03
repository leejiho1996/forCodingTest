# 템포럴 그래프
import sys
input = sys.stdin.readline

N, T, M = map(int,input().split())
S, E = map(int,input().split())
MAX = 10_000_001

# dp
dp = [[MAX] * N for _ in range(T+1)]
dp[0][S] = 0

for i in range(1, T+1):
    for j in range(N):
        dp[i][j] = dp[i-1][j]
        
    for j in range(M):
        n1, n2, w = map(int,input().split())
        dp[i][n1] = min(dp[i][n1], dp[i-1][n2] + w)
        dp[i][n2] = min(dp[i][n2], dp[i-1][n1] + w)
        
if dp[T][E] == MAX:
    print(-1)
else:
    print(dp[T][E])
