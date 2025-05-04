# 팬케이크 쌓기
import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
start = []
sett = set()
target = tuple([i for i in range(1, N+1)])

for i in range(N):
    a, b = input().rstrip().split()

    if b == "+":
        start.append(int(a))
    else:
        start.append(-int(a))

que = deque([])
que.append((tuple(start), 0))

while que:
    cake, cnt = que.popleft()

    if cake == target:
        break

    if cake in sett:
        continue
    else:
        sett.add(cake)

    for i in range(N):
        tmp = list(cake)

        for j in range(i//2+1):
            tmp[j], tmp[i-j] = -tmp[i-j], -tmp[j]

        tmp = tuple(tmp)
        
        if tmp in sett:
            continue
        else:
            que.append((tmp, cnt+1))

print(cnt)