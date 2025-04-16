# AH-Choo!
import sys
input = sys.stdin.readline

N = int(input())
X = list(map(int,input().split()))
Y = list(map(int,input().split()))
dp = [[0]*(N) for _ in range(N)]

dp[0][0] = (X[0] - Y[0])**2
for i in range(1, N):
    dp[0][i] = dp[0][i-1] + (X[0] - Y[i])**2
    
for i in range(1, N):
    for j in range(N):
        if j == 0:
            dp[i][j] = dp[i-1][0]
        else:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])

        dp[i][j] += (X[i] - Y[j])**2

        if i == N-1:
            for k in range(j+1, N):
                dp[i][j] += (X[N-1] - Y[k])**2

minn = float('inf')
for i in range(N):
    minn = min(minn, dp[N-1][i])

print(minn)
