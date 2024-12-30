# ATM
import sys
input = sys.stdin.readline
sys.setrecursionlimit(5000001)

def tarjan(n):
    global nodeCnt
    global sccCnt
    
    stack.append(n)
    discovered[n] = nodeCnt
    ret = nodeCnt
    nodeCnt += 1

    for child in graph[n]:
        if not discovered[child]:
            ret = min(ret, tarjan(child))
        elif not sccGroup[child]:
            ret = min(ret, discovered[child])

    if ret == discovered[n]:
        while stack:
            cur = stack.pop()
            sccGroup[cur] = sccCnt
            sccCash[sccCnt] += cash[cur]

            if isRestaurant[cur]:
                hasRestaurant[sccCnt] = 1
                
            if cur == n:
                sccCnt += 1
                break
    return ret

def dfs(n, total):
    result = 0

    if dp[n] != -1:
        return dp[n]
    
    for i in sccGraph[n]:
        result = max(result, dfs(i, total))
    
    if hasRestaurant[n] or result > 0:
        result += sccCash[n]

    dp[n] = result
    return result

# 입력관련 변수
n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]
cash = [0] * (n+1)
isRestaurant = [0] * (n+1)

# SCC관련 변수
sccGraph = [[] for _ in range(n+1)]
sccCash = [0] * (n+1)
stack = []
discovered = [0] * (n+1)
sccGroup = [0] * (n+1)
hasRestaurant = [0] * (n+1)
nodeCnt = 1
sccCnt = 1

for i in range(m):
    start, to  = map(int,input().split())
    graph[start].append(to)

for i in range(n):
    cash[i+1] = int(input())

start, restaurant = map(int,input().split())

for i in list(map(int,input().split())):
    isRestaurant[i] = 1    

for i in range(1, n+1):
    if not discovered[i]:
        tarjan(i)

for i in range(1, n+1):
    for j in graph[i]:
        if sccGroup[i] != sccGroup[j]:
            sccGraph[sccGroup[i]].append(sccGroup[j])

dp = [-1] * sccCnt
print(dfs(sccGroup[start], 0))
