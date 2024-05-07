#알고리즘 수업 - bfs1
import sys
from collections import deque
input = sys.stdin.readline

n, m, r = map(int,input().split())

graph = [[] for _ in range(n)]

for i in range(m):
    start, to = map(int,input().split())

    graph[start-1].append(to-1)
    graph[to-1].append(start-1)

que = deque([])
visited = [0] * n
cnt = 1
visited[r-1] = 1

for i in sorted(graph[r-1]):
    que.append(i)


while que:
    to = que.popleft()

    if visited[to]:
        continue

    cnt += 1
    visited[to] = cnt

    for i in sorted(graph[to]):
        if not visited[i]:
            que.append(i)

for i in visited:
    print(i)
