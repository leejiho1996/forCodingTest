# 십자 찾기
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
K = int(input())

graph = []
row = [[0] * (M+1) for _ in range(N)]
col = [[0] * (N+1) for _ in range(M)]
result = 0

for i in range(N):
    cur = list(map(int,input().split()))
    graph.append(cur)
    
    for j in range(M):
        row[i][j+1] = row[i][j] + cur[j]
        col[j][i+1] = col[j][i] + cur[j]

for i in range(N):
    for j in range(M):
        if i - K < 0 or i + K >= N or j - K < 0 or j + K >= M:
            continue

        if graph[i][j] == 0:
            continue
        
        total = 0

        total += row[i][j+K+1] - row[i][j+1]
        total += row[i][j] - row[i][j-K]
        total += col[j][i+K+1] - col[j][i+1]
        total += col[j][i] - col[j][i-K]

        if total == 4*K:
            result += 1

print(result)
        
