# 마라톤2
import sys
input = sys.stdin.readline

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
            solve(e-i-1, k-i) +
            abs(points[e][0] - points[e-i-1][0]) + abs(points[e][1] - points[e-i-1][1]))

    return dp[e][k]

N, K = map(int,input().split())
points = []
dp = [[-1] * (K+1) for _ in range(N)]
dist = [0] * (N+1)

for i in range(N):
    x, y = map(int,input().split())
    points.append((x, y))

    if i != 0:
        dist[i] = dist[i-1] + abs(points[i-1][0] - x) + abs(points[i-1][1] - y)

print(solve(N-1, K))
