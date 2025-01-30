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
    

    min_dp[0] = min(min_tmp[0], min_tmp[1]) + num[0]
    max_dp[0] = max(max_tmp[0], max_tmp[1]) + num[0]
       
    min_dp[1] = min(min_tmp[0], min_tmp[1], min_tmp[2]) + num[1]
    max_dp[1] = max(max_tmp[0], max_tmp[1], max_tmp[2]) + num[1]
        
    min_dp[2] = min(min_tmp[1], min_tmp[2]) + num[2]
    max_dp[2] = max(max_tmp[1], max_tmp[2]) + num[2]

print(max(max_dp), min(min_dp))
