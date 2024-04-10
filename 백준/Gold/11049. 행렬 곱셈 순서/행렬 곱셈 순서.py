# 행렬 곱셈 순서
import sys
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]

limit = pow(2, 30) - 1
dp = [[limit] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = 0
    
def sequence():
    for i in range(1, n):
        for j in range(n-i):
            # start와 end 정하기
            start = j
            end = i + j
            for mid in range(start, end):
                dp[start][end] = min(dp[start][end],
                                     dp[start][mid] + dp[mid+1][end] # start에서 mid까지, mid에서 start까지 합
                                     + matrix[start][0]*matrix[mid+1][0]*matrix[end][1]) # 합쳐지는 부분의 행렬곱
    print(dp[0][n-1])

sequence()
