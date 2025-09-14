# 환승
import sys
input = sys.stdin.readline
from collections import deque

N, K, M = map(int,input().split())
graph = [[] for _ in range(N+1)]
links = []
visited = [0] * M

for i in range(M):
    link = list(map(int, input().split()))
    links.append(link)
    for j in link:
        graph[j].append(i)

def bfs():
    
    que = deque([])

    if N == 1:
        print(1)
        return
        
    for i in graph[1]:
        que.append((i, 2))
        visited[i] = 1

    while que:
        cur, cnt = que.popleft()
        
        for i in links[cur]:
            if i == N:
                print(cnt)
                return
                
            for j in graph[i]:

                if visited[j]:
                    continue

                que.append((j, cnt+1))
                visited[j] = 1

    print(-1)

bfs()
