# 할로윈의 양아치
import sys
input = sys.stdin.readline

def find(n):
    if friends[n] != n:
        friends[n] = find(friends[n])

    return friends[n]

N, M, K = map(int,input().split())
candies = [0] + list(map(int,input().split()))
friends = [i for i in range(N+1)]
groupCnt = [1] * (N+1)

for i in range(M):
    f1, f2 = map(int,input().split())
    p1 = find(f1)
    p2 = find(f2)

    if p1 != p2:
        friends[p1] = p2
        candies[p2] += candies[p1]
        candies[p1] = 0
        groupCnt[p2] += groupCnt[p1]
        groupCnt[p1] = 0

groupCnt = [groupCnt[i] for i in range(1, N+1) if groupCnt[i] > 0]
candies = [candies[i] for i in range(1, N+1) if candies[i] > 0]
dp = [0] * (K+1)

for i in range(len(groupCnt)):
    for j in range(K, groupCnt[i], -1):
        dp[j] = max(dp[j], dp[j-groupCnt[i]] + candies[i])

print(max(dp))
