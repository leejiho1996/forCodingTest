# 개미
import sys
input = sys.stdin.readline
import math

def dfs(n):
    
    visited[n] = 1

    for i, cost in graph[n]:
        if visited[i]:
            continue
        else:
            dp[i][0] = n
            dist[i][0] = cost
            dfs(i)

n = int(input())
LOG = int(math.log(n, 2))
energy = []
visited = [0] * (n+1)
graph = [[] for _ in range(n+1)]
dp = [[0] * (LOG+1) for _ in range(n+1)] # dp[i][j]는 노드i의 2^j번째 부모노드
dist = [[0] * (LOG+1) for _ in range(n+1)] # 2^j 부모노드까지 거리
dist[1][0] = 1000001

for i in range(n):
    energy.append(int(input()))

for i in range(n-1):
    n1, n2, cost = map(int,input().split())
    graph[n1].append((n2, cost))
    graph[n2].append((n1, cost))

dfs(1)

for i in range(1, LOG+1):
    for j in range(1, n+1):
        dp[j][i] = dp[dp[j][i-1]][i-1]
        dist[j][i] = dist[j][i-1] + dist[dp[j][i-1]][i-1]

for i in range(1, n+1):
    cur = i
    cur_energy = energy[cur-1]
    
    for j in range(LOG, -1, -1):
        if dist[cur][j] <= cur_energy:
            cur_energy -= dist[cur][j]
            cur = dp[cur][j]

        if cur == 1:
            break

    print(cur)
