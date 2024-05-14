# 트리의 지름
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10001)

n = int(input())

tree = [[] for _ in range(n+1)]

for i in range(n-1):
    parent, child, cost = map(int,input().split())
    tree[parent].append((child, cost))
    tree[child].append((parent, cost))

max_node = 0
maxx = 0

def dfs(node, cur):
    global max_node
    global maxx
    
    if not visited[node]:
        visited[node] = 1
        
    if cur > maxx:
        maxx = cur
        max_node = node
    
    for next_node, cost in tree[node]:
        if not visited[next_node]:
            visited[next_node] = 1
            dfs(next_node, cur+cost)

visited = [0] * (n+1)
dfs(1, 0)

visited = [0] * (n+1)
dfs(max_node, 0)

print(maxx)
    
    
