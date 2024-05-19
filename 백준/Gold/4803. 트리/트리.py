# 트리
import sys
input = sys.stdin.readline

def cycle(prev, node):

    if visited[node]:
        return 0
    else:  
        visited[node] = 1

    for i in graph[node]:
        if i == prev:
            continue

        check = cycle(node, i)

        if not check:
            return 0

    return 1

Case = 0

while True:
    n, m = map(int,input().split())
    Case += 1
    if n == 0 and m == 0:
        break

    graph = [[] for _ in range(n+1)]
    cnt = 0
    
    for i in range(m):
        start, to = map(int,input().split())
        graph[start].append(to)
        graph[to].append(start)

    visited = [0] * (n+1)

    for i in range(1, n+1):
        if visited[i]:
            continue
        cnt += cycle(0, i)

    if cnt > 1:
        print(f'Case {Case}: A forest of {cnt} trees.')
    elif cnt == 1:
        print(f'Case {Case}: There is one tree.')
    else:
        print(f'Case {Case}: No trees.')
        

