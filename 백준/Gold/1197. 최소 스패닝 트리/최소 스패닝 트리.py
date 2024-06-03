# 최소 스패닝 트리
import sys
input = sys.stdin.readline
import heapq
sys.setrecursionlimit(100001)

v, e = map(int,input().split())

check = [i for i in range(0, v+1)]

def find(n):
    if check[n] != n:
        check[n] = find(check[n])
    return check[n]
    
que = []
total = 0

for i in range(e):
    start, to, cost = map(int,input().split())
    heapq.heappush(que,(cost, start, to))

while que:
    cost, start, to = heapq.heappop(que)

    start_root = find(start)
    to_root = find(to)

    if start_root == to_root:
        continue
    else:
        check[to_root] = start_root
        total += cost

print(total)
