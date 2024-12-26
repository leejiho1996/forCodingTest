# Strongly Connected Component
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10001)

def dfs(n):
    visited[n] = 1

    for i in graph[n]:
        if visited[i]:
            continue
        else:
            dfs(i)
    
    order.append(n)
    
v, e = map(int,input().split())
graph = [[] for _ in range(v+1)]
graphR = [[] for _ in range(v+1)]
visited = [0] * (v+1)
order = []
result = []

for i in range(e):
    start, to = map(int,input().split())
    graph[start].append(to)
    graphR[to].append(start)
    
for i in range(1, v+1):
    if visited[i]:
        continue
    else:
        dfs(i)

visited = [0] * (v+1)
for i in range(v-1, -1, -1):
    node = order[i]
    scc = []
    if visited[node]:
        continue
    
    stack = [node]
    while stack:
        cur = stack.pop()

        if visited[cur]:
            continue
        else:
            visited[cur] = 1
            scc.append(cur)

        for j in graphR[cur]:
            if visited[j]:
                continue
            else:
                stack.append(j)
    scc.sort()
    scc.append(-1)
    result.append(scc)

result.sort()
print(len(result))
for i in result:
    print(*i)
    
