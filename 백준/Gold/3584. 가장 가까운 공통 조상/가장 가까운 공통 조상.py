# 가장 가까운 공통 조상
import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    parent = [-1] * (n+1)
    visited = [0] * (n+1)
    
    for j in range(n-1):
        p, c = map(int,input().split())
        parent[c] = p

    a, b = map(int,input().split())

    stack_a = [a]
    stack_b = [b]

    while stack_a:
        p_a = stack_a.pop()
        visited[p_a] = 1

        if parent[p_a] != -1:
            stack_a.append(parent[p_a])

    while stack_b:
        p_b = stack_b.pop()

        if visited[p_b]:
            print(p_b)
            break

        stack_b.append(parent[p_b])
