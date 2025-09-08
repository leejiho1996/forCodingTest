# 노드사이의 거리
import sys
input = sys.stdin.readline

def dfs(n, target, dist):

    visited[n] = 1
    ret = 0

    if n == target:
        print(dist)
        return
    
    for i, d in graph[n]:
        if visited[i]:
            continue

        dfs(i, target, dist + d)

N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]

for i in range(N-1):
    n1, n2, d = map(int,input().split())
    graph[n1].append((n2, d))
    graph[n2].append((n1, d))
    
for i in range(M):
    n1, n2 = map(int,input().split())
    visited = [0] * (N+1)
    dfs(n1, n2, 0)
    
