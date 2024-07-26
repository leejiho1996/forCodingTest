# 문제집
import sys
input = sys.stdin.readline
import heapq

n, m = map(int,input().split())

back = [[] for _ in range(n+1)]
front = [0] * (n+1)
result = []

for i in range(m):
    f, e = map(int,input().split())
    back[f].append(e)
    front[e] += 1

for i in range(1, n+1):
    back[i].sort()

stack = []

for i in range(1, (n+1)):
    if front[i] == 0:
        heapq.heappush(stack, i)

while stack:
    num = heapq.heappop(stack)
    result.append(num)
    for j in back[num]:
        front[j] -= 1
        if front[j] == 0:
            heapq.heappush(stack, j)
        
print(*result)