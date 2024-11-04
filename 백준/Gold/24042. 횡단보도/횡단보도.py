# 횡단보도
import sys
input = sys.stdin.readline
import heapq as hq
import math

n, m = map(int,input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    s, e = map(int,input().split())

    graph[s].append((i, e))
    graph[e].append((i, s))

visited = [0] * (n+1)
visited[1] = 1
min_distance = [float('inf')] * (n+1)
heap = []

for time, to in graph[1]:
    hq.heappush(heap, (time+1, to))

while heap:
    time, cur = hq.heappop(heap)
    
    if cur == n:
        print(time)
        break

    if visited[cur]:
        continue

    visited[cur] = time
    
    for nt, nl in graph[cur]:
       
        if nt > time: # 건널수 있다면 다음 시간은+1 
            next_time = nt + 1
        else: # 아니라면 다음 건널 시간을 계산
            next_time = nt + math.ceil((time - nt) / m) * m + 1 

        if min_distance[nl] < next_time:
            continue
        else:
            min_distance[nl] = next_time
            hq.heappush(heap, (next_time, nl))
