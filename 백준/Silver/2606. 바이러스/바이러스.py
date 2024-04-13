# 바이러스
import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

link = int(input())

graph = [[] * n for _ in range(n)]

for i in range(link):
    s, e = map(int,input().split())

    graph[s-1].append(e-1)
    graph[e-1].append(s-1)

worm = [0] * n
worm[0] = 1

que = deque([0])

while que:
    com = que.popleft()

    for i in graph[com]:
        if  worm[i] == 0:
            que.append(i)
            worm[i] = 1

print(sum(worm)-1)
