# 텀 프로젝트
import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    graph = [0] * (n+1)
    students = list(map(int,input().split()))
    front = [0] * (n+1)
    stack = []
    cnt = 0
    
    for j in range(n):
        graph[j+1] = students[j]
        front[students[j]] += 1
        
    for i in range(1, n+1):
        if front[i] == 0:
            stack.append(i)

    while stack:
        cur = stack.pop()
        cnt += 1

        nex = graph[cur]
        front[nex] -= 1

        if front[nex] == 0:
            stack.append(nex)

    print(cnt)
