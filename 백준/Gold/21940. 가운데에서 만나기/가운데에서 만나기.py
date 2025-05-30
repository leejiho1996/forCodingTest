# 가운데에서 만나기
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
graph = [[float('inf')] * (N+1) for _ in range(N+1)]
result = float('inf')

for i in range(M):
    A, B, T = map(int,input().split())
    graph[A][B] = T

K = int(input())
friends = list(map(int,input().split()))

for i in range(1, N+1):
    graph[i][i] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

nodes = []

for i in range(1, N+1):
    curMax = 0

    for j in friends:
        curMax = max(curMax, graph[j][i] + graph[i][j])

    if curMax < result:
        result = curMax
        nodes = []
        nodes.append(i)
    elif curMax == result:
        nodes.append(i)
    
print(*nodes)
