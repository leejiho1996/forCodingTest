# 숫자 맞추기
import sys
input = sys.stdin.readline

n = int(input())
start = [0] + [int(i) for i in input().rstrip()]
target = [0] + [int(i) for i in input().rstrip()]

dp = [[100000] * 10 for _ in range(n+1)]
seq = [[0] * 10 for _ in range(n+1)]

for i in range(10):
    dp[0][i] = i

for i in range(1, n+1):
    for j in range(10):
        left = (target[i] - start[i] - j + 20) % 10
        right = 10 - left
        nextLeft = (j + left) % 10
        
        # 오른쪽 회전
        if dp[i][j] > dp[i-1][j] + right:
            dp[i][j] = dp[i-1][j] + right
            seq[i][j] = -right # 회전횟수 갱신

        # 왼쪽 회전
        if dp[i][nextLeft] > dp[i-1][j] + left:
            dp[i][nextLeft] = dp[i-1][j] + left
            seq[i][nextLeft] = left # 회전횟수 갱신

result = 100000
resultSeq = []
cnt = n

for i in range(10):
    if result > dp[n][i]:
        result = dp[n][i]
        idx = i

print(result) # 총 회전횟수 출력

while cnt > 0:
    move = seq[cnt][idx]
    resultSeq.append(move)

    if move > 0:
        idx = (idx - move + 10) % 10

    cnt -= 1

for i in range(n):
    print(i+1, resultSeq[n-i-1]) # 숫자 나사번호별 회전횟수 출력
