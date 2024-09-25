# 트리의 두 번째 지름
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())

tree = [[] for _ in range(n+1)]

for i in range(n-1):
    start, to, cost = map(int, input().split())
    tree[start].append((to, cost))
    tree[to].append((start, cost))

visited = [-1] * (n+1)

max_dist = 0
max_node = 0

def dfs(node, dist, oppo = 0):
    global max_dist
    global max_node

    visited[node] = 1
    
    for i in tree[node]:
        to, cost = i

        if to == oppo:
            continue

        if visited[to] != -1:
            continue
        else:
            visited[to] = 1

        if max_dist < cost + dist:
            max_dist = cost + dist
            max_node = to

        dfs(to, cost+dist, oppo)

dfs(1, 0)
first_node = max_node

max_dist = 0
max_node = 0
visited = [-1] * (n+1)
dfs(first_node, 0)
second_node = max_node

max_dist = 0
max_node = 0
visited = [-1] * (n+1)
dfs(first_node, 0, second_node)
first_max = max_dist
first_second_node = max_node

max_dist = 0
max_node = 0
visited = [-1] * (n+1)
dfs(second_node, 0, first_node)
second_max = max_dist
second_second_node = max_node

if first_max > second_max:
    print(first_max)
else:
    print(second_max)
