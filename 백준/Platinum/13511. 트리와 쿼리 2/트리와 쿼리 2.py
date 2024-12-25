# 트리와 쿼리2
import sys
input = sys.stdin.readline
import math
sys.setrecursionlimit(1000001)

    
def calDepth(n, d):
    depth[n] = d
    visited[n] = 1

    for cn, dist in graph[n]:
        if visited[cn] != -1:
            continue
        dp[cn][0] = (n, dist)
        calDepth(cn, d+1)

def findNode(n, dist):
    result = n
    for i in range(LOG, -1, -1):
        if dist >= 1 << i:
            dist -= 1 << i
            result = dp[result][i][0]
        if dist == 0:
            break
        
    return result

def LCA(n1, n2):
    total = 0 # 총 거리 
    dist_n1 = 0 # n1의 몇번째 부모인지 담는 변수
    dist_n2 = 0 # n2의 몇번째 부모인지 담는 변수
    isChange = False
    
    if depth[n1] > depth[n2]:
        n1, n2 = n2, n1
        isChange = True
        
    for i in range(LOG, -1, -1):
        if depth[n2] - depth[n1] >= 1 << i:
            total += dp[n2][i][1]
            dist_n2 += 1 << i
            n2 = dp[n2][i][0]

    if isChange:
        n1, n2 = n2, n1
        dist_n1, dist_n2 = dist_n2, dist_n1
    
    if n1 == n2:
        return (total, n1, dist_n1, dist_n2)

    for i in range(LOG, -1, -1):
        if dp[n1][i][0] != dp[n2][i][0]:
            total += dp[n1][i][1]
            total += dp[n2][i][1]
            dist_n1 += 1 << i
            dist_n2 += 1 << i
            n1 = dp[n1][i][0]
            n2 = dp[n2][i][0]
            
    total += dp[n1][0][1]
    total += dp[n2][0][1]
    return (total, dp[n1][0][0], dist_n1+1, dist_n2+1)

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [-1] * (n+1)
LOG = int(math.log(n, 2))
depth = [0] * (n+1)
# dp[i][j] = i의 2^j번째 (조상노드, 거리)
dp = [[(0, 0)] * (LOG+1) for _ in range(n+1)]

for i in range(n-1):
    n1, n2, dist = map(int,input().split())
    graph[n1].append((n2, dist))
    graph[n2].append((n1, dist))

calDepth(1, 0)
for i in range(1, LOG+1):
    for j in range(1, n+1):
        prev = dp[j][i-1][0]
        dist = dp[j][i-1][1] + dp[prev][i-1][1]
        dp[j][i] = (dp[prev][i-1][0], dist)
        
m = int(input())
for i in range(m):
    cmd = list(map(int,input().split()))
    u = cmd[1]
    k = cmd[2]
    total, parent, dist_n1, dist_n2 = LCA(u, k)
    if cmd[0] == 1:
        print(total)
        continue
    
    seq = cmd[3]
    if dist_n1 + 1 == seq:
        print(parent)
    elif dist_n1 >= seq:
        print(findNode(u, seq - 1))
    else:
        print(findNode(k, dist_n2 - (seq - dist_n1 - 1)))
    
