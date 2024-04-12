# 이분 그래프
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

t = int(input())

def dfs(idx):
    global check
    for i in graph[idx]:

        if visit[i] == 0:
            visit[i] = -visit[idx]
            dfs(i)
            
        else:
            if visit[i] == visit[idx]:
                check = False
                return 
        
for i in range(t):
    v, e = map(int,input().split())

    graph = [[] * v for _ in range(v)]
    
    for j in range(e):
        n1, n2 = map(int,input().split())
        graph[n1-1].append(n2-1)
        graph[n2-1].append(n1-1)

    visit = [0] * v
    check = True
    
    for idx in range(v):
        stack = []
        if visit[idx] == 0:
            visit[idx] = 1
            dfs(idx)
            if not check:
                break

    if check:
        print("YES")
    else:
        print("NO")
