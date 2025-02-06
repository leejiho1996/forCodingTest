# 외판원 순회
import sys
input = sys.stdin.readline

n = int(input())
board = []
# 방문도시를 비트 마스킹으로 표기하기 때문에 2^n 개 필요
# dp[cur][visit] = 현재 cur도시이며 방문현황은 visit과 같고,
# 아직 방문하지 않은 도시들을 모두 거쳐 다시 시작점으로 돌아가는데 드는 최소 비용
dp = [[-1] * (2**n) for _ in range(n)] 

for i in range(n):
    board.append(list(map(int,input().split())))

def dfs(x, visited):
    if visited == (1 << n) - 1:
        if board[x][0]:
            return board[x][0]
        else:
            return float('inf')
        
    # dp[x][visited] -1이 아니면 이미 최소값을 찾은거다!
    if dp[x][visited] != -1: 
        return dp[x][visited]
    else: # 그렇지 않다면 우선 최댓값으로 갱신
        dp[x][visited] = 16000000

    for i in range(n):
        if board[x][i] == 0:
            continue

        if visited & (1 << i):
            continue

        dp[x][visited] = min(dp[x][visited], board[x][i] + dfs(i, (visited | 1 << i )))

    # 방문할 수 있는 도시가 없는 경우 (길이 없는 경우도 있음)
    if dp[x][visited] == -1:
        return 16000000

    return dp[x][visited]

print(dfs(0, 1))
