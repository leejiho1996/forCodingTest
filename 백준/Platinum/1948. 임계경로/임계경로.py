# 임계경로
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

dist = [0] * (n+1)
graph = [[] for _ in range(n+1)]
r_graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
visited = [0] * m

for i in range(m):
    s, t, c = map(int,input().split())
    graph[s].append((t, c, i))
    r_graph[t].append((s, c, i))
    indegree[t] += 1
    
start, end = map(int,input().split())

stack = [start]
while stack:
    cur = stack.pop()

    for t, c, i in graph[cur]:
        indegree[t] -= 1
        dist[t] = max(dist[t], dist[cur] + c)

        if indegree[t] == 0:
            stack.append(t)

stack = [end]
while stack:
    cur = stack.pop()
    
    for t, c, i in r_graph[cur]:
        if dist[t] + c == dist[cur]:
            if not visited[i]:
                stack.append(t)
                visited[i] = 1
        
print(dist[end])
print(sum(visited))
