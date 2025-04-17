# Cow Contest
import sys
input = sys.stdin.readline

def dfs(n, graph):
    global cnt
    
    visited[n] = 1
    cnt += 1
    
    for i in graph[n]:
        if not visited[i]:
            dfs(i, graph)

N, M = map(int,input().split())
front = [[] for _ in range(N+1)]
back = [[] for _ in range(N+1)]
result = 0

for i in range(M):
    f, b = map(int,input().split())
    front[b].append(f)
    back[f].append(b)

for i in range(1, N+1):
    cnt = -1
    visited = [0] * (N+1)

    dfs(i, front)
    dfs(i, back)

    if cnt == N:
        result += 1

print(result)
