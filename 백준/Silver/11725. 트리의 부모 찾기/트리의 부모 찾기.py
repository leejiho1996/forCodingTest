# 트리의 부모 찾기
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100001)

n = int(input())

parent = [i for i in range(0, n+1)]

graph = [[] for _ in range(n+1)]

for i in range(n-1):
    n1, n2 = map(int,input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
    
def dfs(root):
    
    for i in graph[root]:
        if i != 1 and parent[i] == i:
            parent[i] = root
            dfs(i)

dfs(1)

for i in range(2, n+1):
    print(parent[i])
