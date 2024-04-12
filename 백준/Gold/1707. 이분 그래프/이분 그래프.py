# 이분 그래프
import sys
input = sys.stdin.readline

t = int(input())

def dfs(idx):
    stack = [(idx, 1)]
    
    while stack:
        node, color = stack.pop()    
        visit[node] = color

        for i in graph[node]:
            if visit[i] == 0:
                stack.append((i, -color))

            elif visit[i] != 0:
                if visit[i] != -color:
                    # print(idx, node, i, color)
                    return False
    return True

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
            check = dfs(idx)
            if not check:
                break

    if check:
        print("YES")
    else:
        print("NO")
