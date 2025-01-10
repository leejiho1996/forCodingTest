# Four Squares
import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
dp = [0] * 50001

dp[1] = 1
dp[2] = 2
dp[3] = 3

for i in range(4, n+1):
    result = 4
    square = 1
    while (square**2 <= i):
        result = min(result, dp[i-square**2])
        square += 1

    dp[i] = result + 1

print(dp[n])
