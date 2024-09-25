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

max_dist = 0
max_node = 0

def dfs(node, prev, dist, oppo = 0):
    global max_dist
    global max_node
    
    for i in tree[node]:
        to, cost = i

        if to == oppo or to == prev:
            continue

        if max_dist < cost + dist:
            max_dist = cost + dist
            max_node = to

        dfs(to, node, cost+dist, oppo)

dfs(1, 0, 0)
first_node = max_node

max_dist = 0
dfs(first_node, 0, 0)
second_node = max_node

max_dist = 0
dfs(first_node, 0, 0, second_node)
first_max = max_dist

max_dist = 0
dfs(second_node, 0, 0, first_node)
second_max = max_dist

if first_max > second_max:
    print(first_max)
else:
    print(second_max)
