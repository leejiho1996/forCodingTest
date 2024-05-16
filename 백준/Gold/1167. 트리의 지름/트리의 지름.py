# 트리의 지름
import sys
input = sys.stdin.readline
from collections import deque

que = deque()

v = int(input())
graph = [ [] for _ in range(v+1)]

for i in range(v):
    link = list(map(int,input().split()))

    for idx, j in enumerate(link):
        if j == -1:
            break
        
        if idx == 0:
            node = j
            continue        
        elif idx % 2 == 1:
            linked = j
        elif idx % 2 == 0:
            graph[node].append((linked, j))

maxx = 0
node = 0

def dfs(n, cost):
    global maxx
    global node

    if not visited[n]:
        visited[n] = 1

    if cost > maxx:
        node = n
        maxx = cost

    for next_node, next_cost in graph[n]:
        if not visited[next_node]:
            visited[next_node] = 1
            dfs(next_node, cost + next_cost)
        
visited = [0] * (v+1)
dfs(1, 0)

visited = [0] * (v+1)
dfs(node, 0)

print(maxx)
    
