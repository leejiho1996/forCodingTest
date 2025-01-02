# 방법을 출력하지 않는 숫자 맞추기
import sys
input = sys.stdin.readline

n = int(input())
# dp[i][j] -> i번째 숫자까지 확인했을 때, 여태까지 왼쪽으로 이동횟수가 j번 일때
# target 숫자로 맞추기 위한 이동 횟수
# ex) dp[3][4] -> 3번 숫자까지 target 숫자로 맞췄을 때, 왼쪽으로 이동 횟수가 4번일때 총 이동횟수 
dp = [[1000000] * (10) for _ in range(n+1)] 
start = [0] + [int(i) for i in input().rstrip()]
target = [0] + [int(i) for i in input().rstrip()]
result = 1000000

for i in range(10):
    dp[0][i] = i

for i in range(1, n+1):
    for j in range(10):
        left = (target[i] - start[i] - j + 20) % 10
        right = 10 - left

        dp[i][j] = min(dp[i][j], dp[i-1][j] + right)
        dp[i][(j + left) % 10] = min(dp[i][(j + left) % 10], dp[i-1][j] + left)
    
for i in range(10):
    result = min(result, dp[n][i])

print(result)
