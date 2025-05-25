# 연세워터파크 (deque)
import sys
input=sys.stdin.readline
from collections import deque

N, D = map(int,input().split())

a = list(map(int,input().split()))
a = [0] + a # 맨 앞에 0을 넣어 음수로 시작하는 경우 처리

que=deque()
dp=[0]*(N+1)
que.append(0)

for i in range(1, N+1):
    # D보다 먼 값은 제거
    if que and que[0] < i-D:
        que.popleft()

    # que의 맨 앞의 값은 D범위 안의 최대값
    if que:
        dp[i] = max(dp[que[0]]+a[i],a[i])
    else:
        dp[i]=a[i]

    # dp[i] 값보다 작은 값들을 제거
    while que and dp[que[-1]] <= dp[i]:
        que.pop()

    # 현재 인덱스를 que에 넣어준다
    que.append(i)

dp.pop(0)

print(max(dp))
