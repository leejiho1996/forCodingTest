# 서강그라운드
import sys
input = sys.stdin.readline

n, m, r = map(int,input().split())
items = [0] + list(map(int,input().split()))
dist = [[2001]*(n+1) for _ in range(n+1)] 
result = 0

for i in range(r):
    start, to, cost = map(int,input().split())
    dist[start][to] = cost
    dist[to][start] = cost

for k in range(1, n+1):
    dist[k][k] = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

for i in range(1, n+1):
    total = 0
    for j in range(1, n+1):
        if dist[i][j] <= m:
            total += items[j]
    result = max(result, total)

print(result)
