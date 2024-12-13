# 도로 네트워크
import sys
input = sys.stdin.readline
import math
sys.setrecursionlimit(1000001)

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [-1] * (n+1)
LOG = int(math.log(n, 2))
depth = [0] * (n+1)
# dp[i][j] = i의 2^j번째 (조상노드, 최소길이, 최대길이)
dp = [[(0, 0, 0)] * (LOG+1) for _ in range(n+1)]

for i in range(n-1):
    n1, n2, dist = map(int,input().split())
    graph[n1].append((n2, dist))
    graph[n2].append((n1, dist))

def calDepth(n, d):
    depth[n] = d
    visited[n] = 1

    for cn, dist in graph[n]:
        if visited[cn] != -1:
            continue
        dp[cn][0] = (n, dist, dist)
        calDepth(cn, d+1)

def LCA(n1, n2):
    minn = float('inf')
    maxx = 0
    
    if depth[n1] > depth[n2]:
        n1, n2 = n2, n1

    for i in range(LOG, -1, -1):
        if depth[n2] - depth[n1] >= 1 << i:
            minn = min(minn, dp[n2][i][1])
            maxx = max(maxx, dp[n2][i][2])
            n2 = dp[n2][i][0]
            
    if n1 == n2:
        return (minn, maxx)

    for i in range(LOG, -1, -1):
        if dp[n1][i][0] != dp[n2][i][0]:
            minn = min(minn, dp[n1][i][1], dp[n2][i][1])
            maxx = max(maxx, dp[n1][i][2], dp[n2][i][2])
            n1 = dp[n1][i][0]
            n2 = dp[n2][i][0]
            
    minn = min(minn, dp[n1][0][1], dp[n2][0][1])
    maxx = max(maxx, dp[n1][0][2], dp[n2][0][2])
    return (minn, maxx)

calDepth(1, 0)
for i in range(1, LOG+1):
    for j in range(1, n+1):
        prev = dp[dp[j][i-1][0]][i-1]
        dp[j][i] = (prev[0],
                    min(dp[j][i-1][1], prev[1]),
                    max(dp[j][i-1][2], prev[2]))
        
k = int(input())
for i in range(k):
    n1, n2 = map(int,input().split())
    print(*LCA(n1, n2))
