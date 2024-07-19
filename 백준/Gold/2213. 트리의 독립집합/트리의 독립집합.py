#트리의 독립집합
import sys
input = sys.stdin.readline

n = int(input())

weights = [0] + list(map(int,input().split()))
tree = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for i in range(n-1):
    start, end = map(int,input().split())
    tree[start].append(end)
    tree[end].append(start)

def dfs(n):
    visited[n] = 1
    
    noSelectWeight = 0
    selectWeight = weights[n]
    noSelectArr = []
    selectArr = [n]

    for i in (tree[n]):
        if visited[i]:
            continue
        
        nextNoSelectWeight, nextSelectWeight, nextNoSelectArr, nextSelectArr = dfs(i)

        selectWeight += nextNoSelectWeight
        selectArr += nextNoSelectArr

        if nextNoSelectWeight > nextSelectWeight:
            noSelectWeight += nextNoSelectWeight
            noSelectArr += nextNoSelectArr
        else:
            noSelectWeight += nextSelectWeight
            noSelectArr += nextSelectArr

    return noSelectWeight, selectWeight, noSelectArr, selectArr

nsw, sw, nsa, sa = dfs(1)

if nsw > sw:
    print(nsw)
    nsa.sort()
    print(*nsa, sep=' ')
else:
    print(sw)
    sa.sort()
    print(*sa, sep = ' ')
