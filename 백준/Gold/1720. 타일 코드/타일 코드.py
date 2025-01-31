# 타일 코드
import sys
input = sys.stdin.readline

n = int(input())
dp = [1] * 31 # 완전 대칭인 타일의 갯수
dp[2] = 3

dpOrigin = [0] * 31 # 모든 타일의 갯수
dpOrigin[1] = 1
dpOrigin[2] = 3


for i in range(3, n+1):
    dpOrigin[i] = dpOrigin[i-1] + dpOrigin[i-2] * 2

for i in range(4, n+1):
    dp[i] = dp[i-2] + dp[i-4] * 2


print(dpOrigin[n] - (dpOrigin[n] - dp[n]) // 2)
