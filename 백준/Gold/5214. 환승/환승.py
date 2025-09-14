# 환승
import sys
input = sys.stdin.readline
from collections import deque

N, K, M = map(int,input().split())
graph = []
g_visited = [0] * M
visited = [0] * (N+1)

for i in range(M):
    links = set(map(int,input().split()))
    graph.append(links)
    
que = deque([])
que.append((1, 1))
visited[1] = 1

while que:
    cur, cnt = que.popleft()
    
    if cur == N:
        print(cnt)
        exit()
        
    for i in range(M):
        if g_visited[i]:
            continue

        sett = graph[i]
        
        if cur in sett:
            for j in sett:
                if visited[j]:
                    continue

                que.append((j, cnt+1))
                visited[j] = 1

            g_visited[i] = 1

print(-1)
