# 거짓말
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
truth = set(list(map(int,input().split()))[1:])
visited = [0] * (n+1)
graph = [[0] * (n+1) for _ in range(n+1)]
party = [[]]
result = 0

for i in range(m):
    people = list(map(int,input().split()))[1:]
    party.append(people)
    
    for j in people:
        for k in (people):
            if j == k:
                continue
            graph[j][k] = 1
            graph[k][j] = 1

for i in truth:
    stack = [i]

    while stack:
        cur = stack.pop()

        if visited[cur]:
            continue
        else:
            visited[cur] = 1

        for i in range(1, n+1): 
            if graph[cur][i] == 1 and visited[i] == 0:
                stack.append(i)

for i in range(1, m+1):
    check = False
    for j in party[i]:
        if visited[j]:
            check = True
            break

    if not check:
        result += 1

print(result)