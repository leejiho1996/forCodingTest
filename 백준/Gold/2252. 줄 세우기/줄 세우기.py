# 줄 세우기
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
child = [[] for _ in range(n+1)]
count = [0] * (n+1)
stack = []
result = []

for i in range(m):
    A, B = map(int,input().split())
    count[B] += 1
    child[A].append(B)

for i in range(1, n+1):
    if not count[i]:
        stack.append(i)

while stack:
    cur = stack.pop()
    result.append(cur)

    for i in child[cur]:
        count[i] -= 1

        if not count[i]:
            stack.append(i)

print(*result)
