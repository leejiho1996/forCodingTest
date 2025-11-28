# 마라톤2
import sys
input = sys.stdin.readline

def cal(p1, p2):
    return abs(points[p1][0]-points[p2][0]) + abs(points[p1][1]-points[p2][1])

def solve(e, k):

    if e == 0:
        return 0
    
    if dp[e][k] != -1:
        return dp[e][k]
        
    dp[e][k] = float('inf')

    for i in range(0, k+1):

        if e-i-1 < 0:
            break
        
        dp[e][k] = min(
            dp[e][k],
            solve(e-i-1, k-i) + cal(e, e-i-1))

    return dp[e][k]

N, K = map(int,input().split())
points = []
dp = [[-1] * (K+1) for _ in range(N)]

for i in range(N):
    x, y = map(int,input().split())
    points.append((x, y))

print(solve(N-1, K))
