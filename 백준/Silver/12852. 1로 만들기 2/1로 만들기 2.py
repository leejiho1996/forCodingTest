# 1로 만들기 2
import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

visited = [-1] * (1000001)

que = deque([])
que.append((n, 0))

while que:
    num, cnt = que.popleft()

    if num == 1:
        print(cnt)
        break
    
    if num % 3 == 0 and visited[num//3] == -1:
        que.append((num//3, cnt+1))
        visited[num//3] = num

    if num % 2 == 0 and visited[num//2] == -1:
        que.append((num//2, cnt+1))
        visited[num//2] = num

    if num - 1 > 0 and visited[num-1] == -1:
        que.append((num-1, cnt+1))
        visited[num-1] = num

start = 1
result = [1]

while start != n:
    start = visited[start]
    result.append(start)

print(*result[::-1])
