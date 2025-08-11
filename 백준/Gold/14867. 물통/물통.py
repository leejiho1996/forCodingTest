# 물통
import sys
input = sys.stdin.readline
from collections import deque

A, B, C, D = map(int,input().split())

visited = set()

que = deque([])
que.append((0, 0, 0))

while que:
    a, b, cnt = que.popleft()

    if a == C and b == D:
        print(cnt)
        exit()

    if (A, b) not in visited:
        que.append((A, b, cnt+1))
        visited.add((A, b))

    if (a, B) not in visited:
        que.append((a, B, cnt+1))
        visited.add((a, B))

    four_to_b = (max(0, a-(B-b)), min(B, b+a))
    four_to_a = (min(A, a+b), max(0, b - (A-a)))
    
    if four_to_b not in visited:
        que.append((four_to_b[0], four_to_b[1], cnt+1))
        visited.add(four_to_b)

    if four_to_a not in visited:
        que.append((four_to_a[0], four_to_a[1], cnt+1))
        visited.add(four_to_a)

    if (0, b) not in visited:
        que.append((0, b, cnt+1))
        visited.add((0, b))

    if (a, 0) not in visited:
        que.append((a, 0, cnt+1))
        visited.add((a, 0))

print(-1)
