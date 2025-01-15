# 철로
import sys
input = sys.stdin.readline
import heapq as hq

n = int(input())
location = []
que = []
result = 0

for i in range(n):
    h, o = map(int,input().split())

    if h > o:
        h, o = o, h

    location.append((h, o))

d = int(input())

location.sort(key = lambda x : (x[1], x[0]))

for i in range(n):
    h = location[i][0]
    limit = h + d

for i in range(n):
    start, end = location[i]
    limit = end - d

    hq.heappush(que, start)

    while que and que[0] < limit:
        hq.heappop(que)

    result = max(result, len(que))

print(result)
