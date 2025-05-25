# 연세워터파크 (deque)
import sys
input=sys.stdin.readline
from collections import deque

N, D = map(int,input().split())

bridges = list(map(int,input().split()))

que = deque([])
#que.append(0)

dp = [0]*(N)

for i in range(N):
    # D보다 먼 값은 제거
    if que and que[0] < i-D:
        que.popleft()

    # que의 맨 앞의 값은 D범위 안의 최대값
    if que:
        dp[i] = max(dp[que[0]] + bridges[i], bridges[i])
    else:
        dp[i] = bridges[i]

    # dp[i] 값보다 작은 값들을 제거
    while que and dp[que[-1]] <= dp[i]:
        que.pop()

    # 현재 인덱스를 que에 넣어준다
    que.append(i)

print(max(dp))
