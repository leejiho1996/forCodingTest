# 정점들의 거리
import sys
import math
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(n, dep):
    depth[n] = dep
    
    for c, d in graph[n]:
        if depth[c] != -1:
            continue
        else:
            parent[c][0] = n
            dist[c][0] = d
            dfs(c, dep+1)

def findLCA(n1, n2):
    total = 0
    
    if depth[n1] < depth[n2]:
        n1, n2 = n2, n1

    # depth 맞춰주기
    for i in range(LOG, -1, -1):
        if depth[parent[n1][i]] >= depth[n2]:
            total += dist[n1][i]
            n1 = parent[n1][i]

    if n1 == n2:
        return total

    # LCA 찾기
    for i in range(LOG, -1, -1):
        if parent[n1][i] != parent[n2][i]:
            total += dist[n1][i] + dist[n2][i]
            
            n1 = parent[n1][i]
            n2 = parent[n2][i]

    return total + dist[n1][0] + dist[n2][0]  

N = int(input())
LOG = int(math.log(N,2))
graph = [[] for _ in range(N+1)]
parent = [[0]*(LOG+1) for _ in range(N+1)]
dist = [[0]*(LOG+1) for _ in range(N+1)]
depth = [-1] * (N+1)

for i in range(N-1):
    a, b, d = map(int,input().split())
    graph[a].append((b, d))
    graph[b].append((a, d))

# 1번 노드를 부모로 dfs 수행하며 깊이 계산
dfs(1, 0) 

for i in range(1, LOG+1):
    for j in range(1, N+1):
        last = parent[j][i-1] # 2^(i-1)번째 부모
        parent[j][i] = parent[last][i-1]
        dist[j][i] = dist[j][i-1] + dist[last][i-1]

# M 입력
M = int(input())
for i in range(M):
    n1, n2 = map(int,input().split())
    print(findLCA(n1, n2))
