# 파괴된 도시
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
result = []

for i in range(M):
    a, b = map(int,input().split())

    graph[a].append(b)
    graph[b].append(a)

K = int(input())
broken = list(map(int,input().split()))
broken.sort()

for i in broken:
    visited[i] = 1

possible = set()
for i in broken:
    check = False

    for j in graph[i]:
        if visited[j] == 0:
            check = True
            break

    if not check:
        possible.add(i)
        result.append(i)
        for j in graph[i]:
            possible.add(j)

possible = list(possible)
possible.sort()

if possible != broken:
    print(-1)
else:
    print(len(result))
    print(*result)
