# 도시 분할 계획
import sys
input = sys.stdin.readline

def find(n):
    if parent[n] != n:
        parent[n] = find(parent[n])

    return parent[n]

n, m = map(int,input().split())
parent = [i for i in range(n+1)]
edges = []
total = 0
maxCost = 0

for i in range(m):
    n1, n2, cost = map(int,input().split())
    edges.append((cost, n1, n2))

edges.sort(key = lambda x : x[0])

for i in range(m):
    cost, n1, n2 = edges[i]

    p1 = find(n1)
    p2 = find(n2)

    if p1 != p2:
        total += cost
        maxCost = max(maxCost, cost)
        parent[p2] = p1
        
print(total - maxCost)
