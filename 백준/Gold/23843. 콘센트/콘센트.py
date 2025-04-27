# 콘센트
import sys
input = sys.stdin.readline
import heapq as hq

N, M = map(int,input().split())
devices = list(map(int,input().split()))
que = []

devices.sort(reverse=True)
idx = M
time = 0

for i in range(min(M, N)):
    hq.heappush(que, devices[i])

while que:
    time = hq.heappop(que)

    while que and que[0] == time:
        hq.heappop(que)

    while len(que) < M and idx < N:
        hq.heappush(que, devices[idx] + time)
        idx += 1

print(time)
