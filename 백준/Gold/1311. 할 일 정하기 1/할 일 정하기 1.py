# 할일 정하기
import sys
input = sys.stdin.readline

n= int(input())

works = []
for i in range(n):
    works.append(list(map(int,input().split())))

dp = [-1] * (1<<(n+1))

def dfs(cur, visited):
    if cur == n:
        return 0

    if dp[visited] != -1:
        return dp[visited]
    
    for i in range(n):
        if (visited & (1 << i)):
            continue
        
        if dp[visited] == -1:
            dp[visited] = works[cur][i] + dfs(cur+1, visited | 1 << i)
        else:
            dp[visited] = min(dp[visited], dfs(cur+1, visited | 1 << i) + works[cur][i])
        
    return dp[visited]

print(dfs(0,0))
