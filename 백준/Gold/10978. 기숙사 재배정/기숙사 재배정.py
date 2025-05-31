# 기숙사 재배정
import sys
input = sys.stdin.readline

def solve(cur, visit):

    if cur == N:
        if visit == (1 << N) - 1:
            return 1

        return 0

    if dp[cur][visit] != -1:
        return dp[cur][visit]
    else:
        dp[cur][visit] = 0
        
    for i in range(N):
        if visit & (1 << i) or i == cur:
            continue

        dp[cur][visit] += solve(cur+1, visit | (1 << i))

    return dp[cur][visit]
            
T = int(input())

for i in range(T):
    N = int(input())
    dp = [[-1] * (1 << N) for _ in range(N)]
    print(solve(0, 0))
    
