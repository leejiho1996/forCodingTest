# 숨바꼭질
import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
dic = {} # 거리별 노드 저장
max_dist = 0

for i in range(M):
    start, to = map(int,input().split())
    graph[start].append(to)
    graph[to].append(start)

que = deque([])
que.append((1, 0))

while que:
    node, dist = que.popleft()

    if visited[node]:
        continue
    else:
        visited[node] = 1
        max_dist = max(max_dist, dist)

    if dist not in dic:
        dic[dist] = [node]
    else:
        dic[dist].append(node)

    for n in graph[node]:
        if visited[n]:
            continue
        else:
            que.append((n, dist+1))

dic[max_dist].sort()
print(dic[max_dist][0], max_dist, len(dic[max_dist]))
    
