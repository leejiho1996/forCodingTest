# 스티커
import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    # dp[i][j] => i행 j열 까지 스티커를 떼어냈을 때 최대값
    dp = [[0] * (n+1) for _ in range(2)]
    nums = []

    for j in range(2):
        nums.append(list(map(int,input().split())))

    dp[0][1] = nums[0][0]
    dp[1][1] = nums[1][0]
    
    for i in range(2, n+1):
        up = nums[0][i-1]
        down = nums[1][i-1]
        
        dp[0][i] = up + max(dp[1][i-1], dp[1][i-2])
        dp[1][i] = down + max(dp[0][i-1], dp[0][i-2])
        
    print(max(dp[0][n], dp[1][n]))
