# 케빈 베이컨의 6단계 법칙
import sys
input = sys.stdin.readline
from collections import deque

def bfs(n):
    que = deque([(n, 0)])
    result = 0
    while que:
        cur, cnt = que.popleft()

        if visited[cur]:
            continue
        else:
            visited[cur] = 1
            result += cnt

        for i in graph[cur]:
            if not visited[i]:
                que.append((i, cnt+1))
    return result
        

n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]
minn = float('inf')
result = 0

for i in range(m):
    s, t = map(int,input().split())
    graph[s].append(t)
    graph[t].append(s)

for i in range(1, n+1):
    visited = [0] * (n+1)
    cur = bfs(i)
    if minn > cur:
        result = i
        minn = cur

print(result)
