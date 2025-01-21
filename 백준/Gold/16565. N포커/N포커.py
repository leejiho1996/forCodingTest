# N포커
import sys
input = sys.stdin.readline

MOD = 10007
n = int(input())

dp = [[0] * 53 for _ in range(53)]
dp[0][0] = 1

for i in range(1, 53):
    dp[i][0] = 1
    dp[i][i] = 1
    dp[i][1] = i
    for j in range(1, i//2+1):
        dp[i][j] = (dp[i-1][j] + dp[i-1][j-1]) % MOD
        dp[i][i-j] = dp[i][j]

result = 0
for i in range(1, i//4+1):
    if i % 2 == 1:
        result += dp[13][i] * dp[52-i*4][n-i*4] % MOD
    else:
        result -= dp[13][i] * dp[52-i*4][n-i*4] % MOD

print(result % MOD)
