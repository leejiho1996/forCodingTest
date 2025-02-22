# Dance Dance Revolution
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000001)

def dfs(cnt, left, right):
    if cnt == length:
        return 0
    
    if dp[cnt][left][right] != -1:
        return dp[cnt][left][right]
    else:
        dp[cnt][left][right] = 0
        
    cur = commands[cnt]

    if cur == left or cur == right:
        dp[cnt][left][right] +=  1 + dfs(cnt+1,left, right)
    else:
        leftPower = moves[left][cur]
        rightPower = moves[right][cur]
        dp[cnt][left][right] += min(leftPower + dfs(cnt+1, cur, right),
                                    rightPower + dfs(cnt+1, left, cur))

    return dp[cnt][left][right]


commands = list(map(int,input().split()))[:-1]
length = len(commands)

# dp[i][j][k] -> 현재 i번째 지시를 수행하고, 왼발이 j, 오른발이 k일때
# 마지막 지시사항까지 수행했을 때 최소 힘
dp = [[[-1] * 5 for _ in range(5)] for _ in range(length+1)]
moves = [[0] * 5 for _ in range(5)]

for i in range(5):
    for j in range(5):
        if i == 0 or j == 0:
            moves[i][j] = 2
        elif abs(i - j) == 2:
            moves[i][j] = 4
        elif i - j == 0:
            moves[i][j] = 1
        else:
            moves[i][j] = 3

print(dfs(0, 0, 0))
