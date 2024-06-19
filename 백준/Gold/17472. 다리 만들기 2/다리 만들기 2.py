# 다리만들기 2
import sys
input = sys.stdin.readline
import heapq

n, m = map(int,input().split())

island = []
visited = [[0]*m for _ in range(n)]

def find_island(i, j):
    global cnt
    
    if visited[i][j] or island[i][j] == 0:
        return 0
    else:
        island[i][j] = cnt
        visited[i][j] = 1
        for r, c in ((-1,0), (1,0), (0,-1), (0,1)):
            if 0 <= i+r < n and 0 <= j+c < m:
                find_island(i+r, j+c)
        return 1

for i in range(n):
    row = list(map(int,input().split()))
    island.append(row)

cnt = 1
for i in range(n):
    for j in range(m):
        if find_island(i, j):
            cnt += 1

graph = [[float('inf')]*cnt for _ in range(cnt)]
parent = [i for i in range(0, cnt)]

que = []

direction = {'r':(0,1), 'l':(0,-1), 'u':(1,0), 'd':(-1,0)}

def bridge(start, i, j, cost, direc):
    to = island[i][j]
    if cost > 0 and start == to:
        return

    if cost == 2 and to != 0 and start != to:
        return
    
    if to != 0 and to != start and cost-1 >=2 :
        graph[start][to] = min(graph[start][to], cost - 1)
        graph[to][start] = min(graph[to][start], cost - 1)
        return

    r, c = direction[direc]
    if 0 <= i+r < n and 0 <= j+c < m:
        bridge(start, i+r, j+c, cost+1, direc)

def find(n):
    if parent[n] != n:
        parent[n] = find(parent[n])
    return parent[n]
                    
for i in range(n):
    for j in range(m):
        if island[i][j] != 0:
            bridge(island[i][j], i, j, 0, 'r')
            bridge(island[i][j], i, j, 0, 'l')
            bridge(island[i][j], i, j, 0, 'u')
            bridge(island[i][j], i, j, 0, 'd')

for i in range(cnt):
    for j in range(i + 1, cnt):
        if graph[i][j] != float('inf'):
            heapq.heappush(que, (graph[i][j], i, j))

total = 0
link = 0
while que:
    cost, start, to = heapq.heappop(que)

    s_p = find(start)
    t_p = find(to)

    if s_p != t_p:
        if s_p > t_p:
            parent[s_p] = t_p
        else:
            parent[t_p] = s_p

        total += cost
        link += 1

if link == cnt - 2:
    print(total)
else:
    print(-1)
