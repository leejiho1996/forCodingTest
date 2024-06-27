# ACM craft
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
t = int(input())

def dfs(n):
    if dp[n] != -1:
        return
    
    if len(graph[n]) == 0:
        dp[n] = delay[n-1]
        return
    
    for i in (graph[n]):
        if dp[i] != -1:
            dp[n] = max(dp[n], dp[i] + delay[n-1])
            continue
        else:
            dfs(i)
            dp[n] = max(dp[n], dp[i] + delay[n-1])

for i in range(t):
    n, k  = map(int,input().split())
    delay = list(map(int,input().split()))
    dp = [-1] * (n+1)
    graph = [[] for _ in range(n+1)]

    for j in range(k):
        x, y = map(int,input().split())
        graph[y].append(x) # y를 건설하는데 필요한 x

    target = int(input())

    dfs(target)

    print(dp[target])