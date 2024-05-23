# 상근이의 여행
import sys
input = sys.stdin.readline

t = int(input())

def dfs(start):
    global cnt
    
    if visited[start]:
        return
    else:
        visited[start] = 1
    cnt += 1
    
    for i in graph[start]:
        if not visited[i]:
            dfs(i)
            
for i in range(t):
    n, m = map(int,input().split())

    visited = [0] * (n+1)
    graph = [[] for _ in range(n+1)]

    cnt = 0
    
    for j in range(m):
        start, to = map(int,input().split())

        graph[start].append(to)
        graph[to].append(start)

    dfs(start)

    print(cnt-1)
