# 등산 마니아
import sys
input = sys.stdin.readline
sys.setrecursionlimit(3000001)

n = int(input())
graph = [[] for _ in range(n+1)]
nodes = [1] * (n+1)
visited = [0] * (n+1)

for i in range(n-1):
    s, t = map(int,input().split())
    graph[s].append(t)
    graph[t].append(s)

def dfs(n):
    if visited[n]:
        return 0
    visited[n] = 1
    
    for i in graph[n]:
        if visited[i]:
            continue
        nodes[n] += dfs(i)

    return nodes[n]

def edgeCount(n):
    return n * (n-1) // 2

dfs(1)
total = edgeCount(n)
result = 0

for i in range(2, n+1):
    result += total - edgeCount(n - nodes[i])

print(result)

