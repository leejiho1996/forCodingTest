# 물벼룩의 생존확률
import sys
input = sys.stdin.readline

def solve(loc, n):

    if dp[loc][n] != -1:
        return dp[loc][n]
    else:
        dp[loc][n] = 0

    if loc == 0: # 수면에 닿았다면 2^(남은 횟수) 리턴
        dp[loc][n] = 2**n
        return dp[loc][n]

    if n == 0:
        dp[loc][n] = 0
        return 0
    
    dp[loc][n] = solve(loc+1, n-1) + solve(loc-1, n-1)

    return dp[loc][n]

K, N = map(int,input().split())
dp = [[-1] * 64 for _ in range(128)]

print(2**N - solve(K, N))



