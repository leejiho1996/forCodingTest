# 너 봄에는 캡사이신이 맛있단다
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
nums.sort()
MOD = 1_000_000_007
aggSum = [0] # 누적 합
result = 0

for i in range(n):
    aggSum.append((aggSum[i] + nums[i]) % MOD)

for i in range(n-1):
    result += (2**(i) % MOD) * (aggSum[n] - aggSum[i+1] - aggSum[n-1-i]) % MOD
    
print(result % MOD)
