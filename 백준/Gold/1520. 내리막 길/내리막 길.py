# 내리막 길
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

m, n = map(int,input().split())
board = [list(map(int, input().split())) for _ in range(m)]

pos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
dp = [[-1] * n for _ in range(m)]

def dfs(r, c):
    
    if r == m-1 and c == n-1:
        return 1

    dp[r][c] = 0
    
    for n_r, n_c in pos:
        next_r = r + n_r
        next_c = c + n_c
        
        if 0 <= next_r < m and 0 <= next_c < n and board[next_r][next_c] < board[r][c]:
            if dp[next_r][next_c] == -1:
                dp[r][c] += dfs(next_r, next_c)

            elif dp[next_r][next_c] >= 1:
                dp[r][c] += dp[next_r][next_c]

    return dp[r][c]

dfs(0,0)

print(dp[0][0])