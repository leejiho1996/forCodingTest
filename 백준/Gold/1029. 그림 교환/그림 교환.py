# 그림 교환
import sys
input = sys.stdin.readline

def solve(cur, visited, price):

    if dp[cur][visited][price] != -1:
        return dp[cur][visited][price]
    else:
        dp[cur][visited][price] = 1

    for i in range(N):
        if visited & (1 << i):
            continue

        if graph[cur][i] < price:
            continue

        nextt = visited | (1 << i)
        
        dp[cur][visited][price] = max(dp[cur][visited][price],
                               solve(i, nextt, graph[cur][i]) + 1)

    return dp[cur][visited][price]

N = int(input())
# graph[i][j] -> j번 예술가가 i번 예술가에게 그림을 살 때 가격
graph = [[0] * N for _ in range(N)]
# dp[i][j][k] => 현재 소유자가 i이고 지금까지 소유한 사람이 j, 현재가격이 k 일때,
# 소유할 수 있는 최대 사람 수
dp = [[[-1] * 10 for _ in range((1<<N)+1)] for _ in range(N)]

for i in range(N):
    row = input().rstrip()
    for j in range(N):
        graph[i][j] = int(row[j])

print(solve(0, 1, 0))


