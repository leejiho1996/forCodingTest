# 보석 도둑
import sys
input = sys.stdin.readline
import heapq

n, k = map(int,input().split())

gem = []
bag = []

for i in range(n):
    m, v = map(int,input().split())
    gem.append((m,v)) # 무게 m, value v

for i in range(k):
    c = int(input())
    bag.append(c)

gem.sort(key = lambda x : x[0], reverse=True)
bag.sort()
que = []

total = 0

for i in bag:
    while gem and gem[-1][0] <= i:
        m, v = gem.pop()
        heapq.heappush(que, (-v, m))

    if que:
        total -= heapq.heappop(que)[0]

print(total)
