# 알고리즘 수업 - 깊이 우선 탐색 1
import sys
input = sys.stdin.readline
sys.setrecursionlimit(300001)

n, m, r = map(int,input().split())

graph = [[] for _ in range(n)]

visited = [0] * n

for i in range(m):
    start, to = map(int, input().split())
    graph[start-1].append(to-1)
    graph[to-1].append(start-1)

cnt = 0
def dfs(node):
    global cnt
    cnt += 1
    visited[node] = cnt

    for i in sorted(graph[node]):
        if not visited[i]:
            dfs(i)
    
dfs(r-1)

for i in visited:
    print(i)
