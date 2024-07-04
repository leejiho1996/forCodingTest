# 줄 세우기
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100001)

n, m = map(int,input().split())

graph = [[] for _ in range(n+1)]
depth = [[-1, i] for i in range(n+1)]

for i in range(m):
    front, end = map(int,input().split())
    graph[end].append(front)

def dfs(num):
    if depth[num][0] != -1:
        return depth[num][0]

    if len(graph[num]) == 0:
        depth[num][0] = 1
        return 1

    for i in (graph[num]):
        if depth[i][0] != -1:
            depth[num][0] = max(depth[num][0], depth[i][0] + 1)
        else:
            depth[num][0] = max(depth[num][0], dfs(i) + 1)
    
    return depth[num][0]

seq = {}
for i in range(1, n+1):
    num = dfs(i)

depth.sort()

for i in range(1, n+1):
    print(depth[i][1], end=' ')


