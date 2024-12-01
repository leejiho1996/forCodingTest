# 등산 마니아
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
top = [""] * (n+1)
visited = [0] * (n+1)
visited[1] = 1

for i in range(n-1):
    s, t = map(int,input().split())
    graph[s].append(t)
    graph[t].append(s)

stack = []

for i in graph[1]:
    stack.append((i, "1 " + str(i)))

while stack:
    cur, route = stack.pop()

    if visited[cur]:
        continue
    
    top[cur] = route
    visited[cur] = 1

    for i in graph[cur]:
        if visited[i]:
            continue        
        stack.append((i, route + " " + str(i)))

for i in range(2, n+1):
    top[i] = set(top[i].split(" "))

total = 0

for i in range(1, n+1):
    for j in range(i+1, n+1):
        if i == 1:
            total += len(top[j]) - 1
            continue

        total += len(top[j].union(top[i])) - 1

print(total)
