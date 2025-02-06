# 외판원 순회
import sys
input = sys.stdin.readline

n = int(input())
board = []
dp = [[-1] * (1 << n) for _ in range(n)]

for i in range(n):
    board.append(list(map(int,input().split())))

def dfs(x, visited):
    if visited == (1 << n) - 1:
        if board[x][0]:
            return board[x][0]

    if dp[x][visited] != -1:
        return dp[x][visited]
    else:
        dp[x][visited] = float('inf')

    for i in range(n):
        if board[x][i] == 0:
            continue

        if visited & (1 << i):
            continue
        
        dp[x][visited] = min(dp[x][visited], board[x][i] + dfs(i, (visited | 1 << i )))

    return dp[x][visited]

print(dfs(0, 1))
