# 도미노
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100001)

def dfs(n):
    visited[n] = 1

    for i in graph[n]:
        if not visited[i]:
            dfs(i)

    order.append(n)

t = int(input())
for i in range(t):
    n, m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    graphR = [[] for _ in range(n+1)] # 역방향 그래프
    visited = [0] * (n+1)
    group = [0] * (n+1) # scc 그룹
    front = [0] * (n+1) # scc 앞에 있는 scc갯수
    order = []
    cnt = 1 # scc 갯수 카운팅
    result = 0 # 밀어야 하는 횟수
    
    for j in range(m):
        s, t = map(int,input().split())
        graph[s].append(t)
        graphR[t].append(s)

    for j in range(1, n+1):
        if not visited[j]:
            dfs(j)

    visited = [0] * (n+1)
    for j in range(n-1, -1, -1):
        if visited[order[j]]:
            continue
        
        stack = [order[j]]

        while stack:
            cur = stack.pop()
            if visited[cur]:
                continue
            else:
                visited[cur] = 1
                group[cur] = cnt

            for k in graphR[cur]:
                if visited[k]:
                    continue
                else:
                    stack.append(k)
        cnt += 1

    for j in range(1, n+1):
        for k in graph[j]:
            if group[j] == group[k]:
                continue
            else:
                front[group[k]] += 1

    for j in range(1, cnt):
        if front[j] == 0:
            result +=  1

    print(result)

    
