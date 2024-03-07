# 신나는 함수 실행
import sys
input = sys.stdin.readline


limit = 2**20
dp = [[[0]*22 for _ in range(22)] for _ in range(22)]
for i in range(0, 22):
    for j in range(0, 22):
        for k in range(0, 22):
            if i <= 0 or j <= 0 or k <= 0:
                dp[i][j][k] = 1
            elif i > 20 or j > 20 or k >20:
                dp[i][j][k] = limit
            elif i < j and j < k:
                dp[i][j][k] = dp[i][j][k-1] + dp[i][j-1][k-1] - dp[i][j-1][k]
            else:
                dp[i][j][k] = dp[i-1][j][k] + dp[i-1][j-1][k] + dp[i-1][j][k-1] - dp[i-1][j-1][k-1]
            
            
while True:
    a, b, c = map(int,input().split())
    if a == -1 and b == -1 and c == -1:
        break
    if max(min(a,b,c), 0) == 0:
        print(f'w({a}, {b}, {c}) = 1')
    elif max(a,b,c) >20:
        print(f'w({a}, {b}, {c}) = {limit}')
    
    else:
        result = dp[a][b][c]
        print(f'w({a}, {b}, {c}) = {result}')