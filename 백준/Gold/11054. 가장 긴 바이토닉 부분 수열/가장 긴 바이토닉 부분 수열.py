# 가장 긴 바이토닉 부분 수열
import sys
input = sys.stdin.readline

n = int(input())

num = list(map(int,input().split()))

maxx = 0

dp = [1] * n
dp_reverse = [1] * n

for i in range(n):
    for j in range(i):
        if num[j] < num[i]:
            dp[i] = max(dp[i], dp[j] + 1)
    
for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if num[j] < num[i] :
            dp_reverse[i] = max(dp_reverse[i], dp_reverse[j]+1)
        
for i in range(n):
    maxx = max(maxx, dp[i] + dp_reverse[i])

print(maxx-1)