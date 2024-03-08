# 구간합5 (dp)
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]


dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] + arr[i-1][j-1] - dp[i-1][j-1]

for i in range(m):
    s_row, s_col, e_row, e_col = map(int, input().split())

    result = dp[e_row][e_col] - dp[s_row-1][e_col] - dp[e_row][s_col-1] + dp[s_row -1][s_col-1]
    print(result)
