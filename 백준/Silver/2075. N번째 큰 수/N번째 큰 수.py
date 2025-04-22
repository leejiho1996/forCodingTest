# N번째 큰 수
import heapq as hq

N = int(input())
cnt = 0
que = []

for i in range(N):
    row = list(map(int,input().split()))
    for j in range(N):
        hq.heappush(que, row[j])

    while len(que) > N:
        hq.heappop(que)

print(hq.heappop(que))
