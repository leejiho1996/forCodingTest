# 템포럴 그래프
import sys
input = sys.stdin.readline

N, T, M = map(int,input().split())
S, E = map(int,input().split())
MAX = 10_000_001

# 템포럴 그래프 정의
graph = [[[] for _ in range(N)] for _ in range(T+1)]

# dp
dp = [[MAX] * N for _ in range(T+1)]

for i in range(1, T+1):
    for j in range(M):
        n1, n2, w = map(int,input().split())
        graph[i][n1].append((n2, w))
        graph[i][n2].append((n1, w))

dp[0][S] = 0

for t in range(1, T+1):
    for n1 in range(N):
        dp[t][n1] = dp[t-1][n1]

        for n2, w in graph[t][n1]:
            dp[t][n1] = min(dp[t][n1], dp[t-1][n2] + w)

if dp[T][E] == MAX:
    print(-1)
else:
    print(dp[T][E])
