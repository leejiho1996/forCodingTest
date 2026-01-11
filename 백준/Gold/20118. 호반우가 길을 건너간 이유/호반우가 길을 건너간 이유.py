# 호반우가 길을 건너간 이유
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
graph = []
ret = []

for i in range(N):
    row = list(map(int,input().split()))
    graph.append(row)

i = 0
j = 0

while i < N-1:
    ret.append((i, j))
    ret.append((i+1, j))
    
    ret.append((i, j))
    ret.append((i+1, j))

    i += 2

if N % 2 == 0:
    i = N-1
    j = 1
else:
    i = N-1
    j = 0

while j < M-1:
    ret.append((i, j))
    ret.append((i, j+1))

    ret.append((i, j))
    ret.append((i, j+1))

    j += 2

if j-1 != M-1:
    ret.append((i-1, M-1))
    ret.append((i, M-1))

    ret.append((i-1, M-1))
    ret.append((i, M-1))

print(len(ret))

for i in ret:
    print(*i)
    
