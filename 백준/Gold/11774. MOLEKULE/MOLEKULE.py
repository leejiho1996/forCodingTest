# MOLEKULE
import sys
input = sys.stdin.readline

def dfs(n, con, prev):
    direc[n] = con
    
    for i in graph[n]:
        if i == prev:
            continue

        dfs(i, -con + 1, n)
        
N = int(input())
graph = [[] for _ in range(N+1)]
direc = [0] * (N+1)
cmd = []

for i in range(N-1):
    a, b = map(int,input().split())
    cmd.append((a, b))
    graph[a].append(b)
    graph[b].append(a)

dfs(1, 0, -1)

for a, b in cmd:
    print(direc[a])
