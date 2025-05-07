# 욕심쟁이 판다
import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
graph = []
nums = []
visited = [[0] * N for _ in range(N)]
direc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
result = 0

for i in range(N):
    row = list(map(int,input().split()))
    graph.append(row)
    for j in range(N):
        nums.append((row[j], i, j))

nums.sort(reverse = True)

for n, r, c in nums:

    for dx, dy in direc:
        nr, nc = r + dx, c + dy

        if nr < 0 or nc < 0 or nr >= N or nc >= N:
                continue
        elif graph[nr][nc] <= n:
                continue

        visited[r][c] = max(visited[r][c], visited[nr][nc]+1)

for i in range(N):
    for j in range(N):
        result = max(result, visited[i][j])

print(result+1)
    
