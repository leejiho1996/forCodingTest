# 매직 포션
import sys
input = sys.stdin.readline
import heapq as hq

N, K = map(int,input().split())
graph = []
que = []
visited = [float('inf')] * N

for i in range(N):
    row = list(input().rstrip())
    graph.append(list(map(int, row)))

for i in range(1, N):
    hq.heappush(que, (graph[0][i], i, K))
    visited[i] = graph[0][i]
    
    if K > 0:
        hq.heappush(que, (graph[0][i] / 2, i, K-1))
        visited[i] = graph[0][i] / 2

while que:
    dist, cur, potion = hq.heappop(que)
   
    for nex in range(N):
        if nex == cur:
            continue

        if visited[nex] > dist + graph[cur][nex]:
            hq.heappush(que, (dist+graph[cur][nex], nex, potion))
            visited[nex] = dist+graph[cur][nex]

        if potion and visited[nex] > dist + graph[cur][nex] / 2:
            hq.heappush(que, (dist+graph[cur][nex]/2, nex, potion-1))
            visited[nex] = dist+graph[cur][nex]/2

print(visited[1])
