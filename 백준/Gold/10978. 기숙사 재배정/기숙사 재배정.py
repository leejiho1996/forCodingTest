# 기숙사 재배정 (점화식)
import sys
input = sys.stdin.readline

dp = [0] * 21
dp[2] = 1

for i in range(3, 21):
    dp[i] = (i-1) * (dp[i-1] + dp[i-2])

T = int(input())

for i in range(T):
    N = int(input())

    print(dp[N])

