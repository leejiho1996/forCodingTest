# 색종이 올려 놓기
import sys
input = sys.stdin.readline

def dfs(n):
    ret = 1
    
    if dp[n] > 0:
        return dp[n]

    ca, cb = papers[n]

    for i in range(N):
        if visited[i]:
            continue

        na, nb = papers[i]

        if (ca < na or cb < nb) and (ca < nb or cb < na):
            continue
        
        visited[i] = 1
        ret = max(ret, dfs(i)+1)
        visited[i] = 0

    dp[n] = ret
    return dp[n]

N = int(input())
papers = []
dp = [0] * N
visited = [0]*(N)
result = 0

for i in range(N):
    a, b = map(int,input().split())
    papers.append((a,b))

for i in range(N):
    visited[i] = 1
    dfs(i)
    visited[i] = 0

print(max(dp))
            
            
