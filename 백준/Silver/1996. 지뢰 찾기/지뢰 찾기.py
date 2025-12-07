# 지뢰 찾기
import sys
input = sys.stdin.readline

N = int(input())
graph = []
result = []
direc = [(1, 0), (-1, 0), (0, 1), (0, -1),
         (1, 1), (1, -1), (-1, 1), (-1, -1)]

for i in range(N):
    graph.append(input().rstrip())

for i in range(N):
    tmp = ''
    for j in range(N):
        cnt = 0
        if graph[i][j] != ".":
            tmp += "*"
            continue
        
        for dx, dy in direc:

            nx, ny = i + dx, j + dy

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            if graph[nx][ny] != ".":
                cnt += int(graph[nx][ny])

        if cnt >= 10:
            tmp += "M"
        else:
            tmp += str(cnt)

    result.append(tmp)

for i in range(N):
    print(result[i])
