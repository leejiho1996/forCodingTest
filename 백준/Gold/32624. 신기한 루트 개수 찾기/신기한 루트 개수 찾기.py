# 신기한 루트 갯수 찾기
import sys
input = sys.stdin.readline
from collections import deque

N, A, B = map(int,input().split())
visited = [0] * N
graph = [[] for _ in range(N)]

for i in range(N-1):
    n1, n2 = map(int,input().split())
    graph[n1-1].append(n2-1)
    graph[n2-1].append(n1-1)

que = deque([])
que.append((A-1, 0))
visited[A-1] = 1

while que:
    cur, cnt = que.popleft()

    for i in graph[cur]:

        if visited[i]:
            continue

        if i == B-1:
            LCA = cur
            break
        
        que.append((i, cnt+1))
        visited[i] = 1

visited = [0] * N

if LCA != A-1:
    stack = [LCA]
    visited[LCA] = 1
else:
    stack = []
    
result = 0

while stack:
    cur = stack.pop()
    result += 1
    visited[cur] = 1


    for i in graph[cur]:
        if i == A-1 or i == B-1:
            continue

        if visited[i]:
            continue
        
        stack.append(i)

print(result)
