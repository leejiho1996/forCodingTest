# K-POP
import sys
input = sys.stdin.readline
from collections import deque

K = int(input())
result = []

for i in range(int(K**(0.5))+1, 0, -1):
    if K % i == 0:
        c = min(i, K // i)
        p = max(i, K // i)
        break

if c == 1:
    print(K+1)
    
    for i in range(1, K+1):
        print(i, i+1)

    exit()

stack = [i for i in range(p+1, p+c+1)]
parents = deque([])

while stack:

    n1 = stack.pop()
    result.append((p, n1))

    if stack:
        n2 = stack.pop()
        result.append((p, n2))

    parents.append(p)
    p -= 1

while p:

    p1 = parents.popleft()
    result.append((p, p1))

    if parents:
        p2 = parents.popleft()
        result.append((p, p2))

    parents.append(p)
    p -= 1

result.sort()

print(len(result)+1)

for i in result:
    print(*i)
    
