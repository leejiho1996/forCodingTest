# 최솟값 찾기
import sys
input = sys.stdin.readline
from collections import deque

N, L = map(int,input().split())
nums = list(map(int,input().split()))

que = deque([])

dp = [float('inf')] * N

for i in range(N):

    if que and que[0] <= i - L:
        que.popleft()

    if que:
        dp[i] = min(nums[que[0]], nums[i])
    else:
        dp[i] = nums[i]

    while que and nums[que[-1]] > nums[i]:
        que.pop()

    que.append(i)

print(*dp)
