# 내려가기
import sys
input = sys.stdin.readline

n = int(input())
min_dp = [0, 0, 0]
max_dp = [0, 0, 0]

for i in range(n):
    num = list(map(int,input().split()))
    min_tmp = min_dp.copy()
    max_tmp = max_dp.copy()
    
    for j in range(3):
        if j == 0:
            min_dp[j] = min(min_tmp[0], min_tmp[1]) + num[j]
            max_dp[j] = max(max_tmp[0], max_tmp[1]) + num[j]
        elif j == 1:
            min_dp[j] = min(min_tmp[0], min_tmp[1], min_tmp[2]) + num[j]
            max_dp[j] = max(max_tmp[0], max_tmp[1], max_tmp[2]) + num[j]
        else:
            min_dp[j] = min(min_tmp[1], min_tmp[2]) + num[j]
            max_dp[j] = max(max_tmp[1], max_tmp[2]) + num[j]

print(max(max_dp), min(min_dp))
