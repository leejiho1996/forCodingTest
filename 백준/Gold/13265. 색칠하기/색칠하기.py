# 색칠하기
import sys
input = sys.stdin.readline

def dfs(n):
    stack = [(n, 1)]

    while stack:
        cur, cnt = stack.pop()

        if visited[cur] != 0:
            continue
        else:
            visited[cur] = cnt

        for j in graph[cur]:
            if visited[j] == cnt:
                return False

            if visited[j] != 0:
                continue
            else:
                stack.append((j, -cnt))

    return True

T = int(input())

for i in range(T):
    N, M = map(int,input().split())
    graph = [[] for _ in range(N+1)]
    visited = [0] * (N+1)

    for j in range(M):
        s, t = map(int,input().split())
        graph[s].append(t)
        graph[t].append(s)

    check = True
    for i in range(1, N+1):
        if not dfs(i):
            check = False
            break

    if not check:
        print("impossible")
    else:
        print("possible")
    
