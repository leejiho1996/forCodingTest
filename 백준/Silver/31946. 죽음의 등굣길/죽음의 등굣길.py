# 죽음의 등굣길
import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
M = int(input())
graph = []
visited = [[0] * M for _ in range(N)]
operation = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

for i in range(N):
    graph.append(list(map(int,input().split())))

if graph[0][0] != graph[N-1][M-1]:
    print("DEAD")
    exit()

K = int(input())

color = graph[0][0]
que = deque([])
que.append((0, 0))

while que:
    r, c = que.pop()

    if r == N-1 and c == M-1:
        print("ALIVE")
        exit()

    for i in range(K+1):
        for j in range(K-i+1):
            for o1, o2 in operation:
                nr = r + o1*i
                nc = c + o2*j

                if nr < 0 or nc < 0 or nr >= N or nc >= M:
                    continue

                if visited[nr][nc] or color != graph[nr][nc]:
                    continue

                que.append((nr, nc))
                visited[nr][nc] = 1

print("DEAD")
