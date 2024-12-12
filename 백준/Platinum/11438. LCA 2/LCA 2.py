# LCA2 희소행렬
import sys
import math
input = sys.stdin.readline
sys.setrecursionlimit(1000001)

n = int(input())
link = [[] for _ in range(n+1)]
log = int(math.log(n, 2))
dp = [[0] * (log+1) for _ in range(n+1)] # dp[i][j]는 노드i의 2^j번째 부모노드
depth = [0] * (n+1)
visited = [0] * (n+1)

for i in range(n-1):
    n1, n2 = map(int,input().split())
    link[n1].append(n2)
    link[n2].append(n1)

# 깊이 계산
def calDepth(n, d):
    depth[n] = d
    visited[n] = 1
    
    for i in link[n]:
        if visited[i]:
            continue
        dp[i][0] = n # 1번째 (2^0 = 1) 부모 노드
        calDepth(i, d+1)

# LCA 계산
def LCA(n1, n2):
    
    if depth[n1] > depth[n2]:
        n1, n2 = n2, n1

    for i in range(log, -1, -1):
        if depth[n2] - depth[n1] >= (1 << i):
            n2 = dp[n2][i]

    if n1 == n2:
        return n1

    for i in range(log, -1, -1):
        if dp[n1][i] != dp[n2][i]:
            n1 = dp[n1][i]
            n2 = dp[n2][i]

    return dp[n1][0]

calDepth(1, 1)

# 희소행렬만들기
for i in range(1, log+1):
    for j in range(1, n+1):
        dp[j][i] = dp[dp[j][i-1]][i-1]

m = int(input())    
for i in range(m):
    a, b = map(int,input().split())
    print(LCA(a, b))
