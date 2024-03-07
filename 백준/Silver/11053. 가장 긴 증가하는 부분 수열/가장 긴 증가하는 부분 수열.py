# 가장 긴 증가하는 부분 수열
import sys
input = sys.stdin.readline

n = int(input())

num_list = list(map(int,input().split()))

dp = [1]*n

for i in range(n):
    for j in range(0, i):
        if num_list[i] > num_list[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))