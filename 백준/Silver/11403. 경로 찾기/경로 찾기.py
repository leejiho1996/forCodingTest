import sys
input = sys.stdin.readline

n = int(input())
result = [[0] * n for _ in range(n)]
graph = []

for i in range(n):
    row = list(map(int,input().split()))
    graph.append(row)

for i in range(n):
    stack = []
    visited = [0] * n

    for j in range(n):
        if graph[i][j]:
            stack.append(j)

    while stack:
        cur = stack.pop()

        if visited[cur]:
            continue
        else:
            visited[cur] = 1
            result[i][cur] = 1

        for j in range(n):
            if graph[cur][j] and not visited[j]:
                stack.append(j)

for i in range(n):
    print(*result[i])
