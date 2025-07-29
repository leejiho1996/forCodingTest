# 로스팅하는 엠마도 바리스타입니다
import sys
input = sys.stdin.readline

N = int(input())
total = [0] * (N+1)
childs = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    n1, n2, dist = map(int,input().split())
    graph[n1].append((n2, dist))
    graph[n2].append((n1, dist))

def calRoot_iterative(start):
    stack = [(start, -1, 0)]  
    post = []

    while stack:
        cur, parent, dist = stack.pop()
        post.append((cur, parent, dist))
        for neighbor, d in graph[cur]:
            if neighbor == parent:
                continue
            stack.append((neighbor, cur, d))

    for cur, parent, dist in reversed(post):
        cnt = 0
        for neighbor, d in graph[cur]:
            if neighbor == parent:
                continue
            cnt += childs[neighbor] + 1
            total[start] += total[neighbor] + (childs[neighbor] + 1) * d
        childs[cur] = cnt

def calDist_iterative(start):
    stack = [(start, -1, 0)]
    while stack:
        cur, parent, dist = stack.pop()

        if parent != -1:
            shorter = childs[cur] * dist
            longer = (N - childs[cur] - 2) * dist
            total[cur] = total[parent] + longer - shorter

        for neighbor, d in graph[cur]:
            if neighbor == parent:
                continue
            stack.append((neighbor, cur, d))

calRoot_iterative(1)
calDist_iterative(1)

for i in range(1, N+1):
    print(total[i])
