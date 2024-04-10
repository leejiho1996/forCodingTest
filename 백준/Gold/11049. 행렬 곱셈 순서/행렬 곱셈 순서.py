# 행렬 곱셈 순서
import sys
input = sys.stdin.readline

n = int(input())
limit = pow(2, 30) - 1
dp = [[limit]*n for _ in range(n)]

matrix = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    dp[i][i] = 0

for k in range(1, n):
    for i in range(n-k):
        for j in range(i, i + k):
            s, m, e = i, j, i+k
            # print(s,m,e)
            dp[s][e] = min(dp[s][e], dp[s][m] + dp[m+1][e] + matrix[s][0] * matrix[m][1] * matrix[e][1])


print(dp[0][n-1])
