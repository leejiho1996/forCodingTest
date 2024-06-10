# 가장 긴 증가하는 부분 수열4
import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int,input().split()))

dp = [1] * n
seq = [[num[_]] for _ in range(n)]

for i in range(n):
    for j in range(0, i):
        if num[i] > num[j]:
            if dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                seq[i] = seq[j].copy()
                seq[i].append(num[i])

max_idx = dp.index(max(dp))

print(dp[max_idx])
print(*seq[max_idx])
