# 최소비용 구하기 2
import sys
input = sys.stdin.readline
import heapq

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for i in range(m):
    start, to, cost = map(int,input().split())
    graph[start].append((cost, start, to))

t_start, t_to = map(int,input().split())
que = []

if t_start == t_to:
    print(0)
    print(1)
    print(1)
    exit()

for i in graph[t_start]:
    heapq.heappush(que, i)

visited = [(float('inf'), -1, -1)] * (n+1)
visited[t_start] = (-1, -1, t_start)

while que:
    cost, prev, cur = heapq.heappop(que)

    if cur == t_to:
        visited[cur] = (cost, prev, cur)
        break

    if visited[cur][0] > cost:
        visited[cur] = (cost, prev, cur)
        
        for i in graph[cur]:
            n_cost, n_start, n_to = i

            if visited[n_to][0] > n_cost + cost:
                heapq.heappush(que, (n_cost+cost, n_start, n_to))

print(visited[t_to][0])

next_node = visited[t_to][1]
route = [t_to]

while next_node != t_start:
    route.append(next_node)
    next_node = visited[next_node][1]

route.append(t_start)

print(len(route))
print(*route[::-1])
