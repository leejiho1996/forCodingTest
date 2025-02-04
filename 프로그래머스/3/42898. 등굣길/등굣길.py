def solution(m, n, puddles):
    dp = [[0] * (m+1) for _ in range(n+1)] # dp[i][j] => i, j 좌표로 가는 최소루트 갯수
    
    for x, y in puddles:
        dp[y][x] = -1
        
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                dp[1][1] = 1
                continue
            
            if dp[i][j] == -1:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    
    return dp[n][m] % 1000000007