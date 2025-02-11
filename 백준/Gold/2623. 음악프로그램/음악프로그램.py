# 음악프로그램
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
front = [0] * (n+1)
graph = [[] for _ in range(n+1)]
stack = []
result = []

for i in range(m):
    seq = list(map(int,input().split()))
    for j in range(seq[0]):
        if j != seq[0] - 1:
            graph[seq[j+1]].append(seq[j+2])
            front[seq[j+2]] += 1

for i in range(1, n+1):
    if front[i] == 0:
        stack.append(i)

while stack:
    cur = stack.pop()
    result.append(cur)
    
    for i in graph[cur]:
        front[i] -= 1
        if front[i] == 0:
            stack.append(i)


if len(result) == n:
    for i in result:
        print(i)
else:
    print(0)
