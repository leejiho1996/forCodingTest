# 사전
import sys
input = sys.stdin.readline

N, M, K = map(int,input().split())
dp = [[1] * (M+1) for _ in range(N+1)]

# dp테이블 채우기
for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

if dp[N][M] < K:
    print(-1)
    exit()

result = ""
cnt = N + M

while N and M:
        
    if dp[N-1][M] < K:
        result += 'z'
        K -= dp[N-1][M]
        M -= 1
    else:
        result += 'a'
        N -= 1

if N:
    result += 'a' * N
else:
    result += 'z' * M

print(result)
