# Player-based Team Distribution
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().split()))
nums.sort(reverse= True)

plus = 0
minus = 0
plus_cnt = 0

for i in range(N):

    if nums[i] >= 0:
        plus += nums[i]
        plus_cnt += 1
    else:
        to_plus = plus + nums[i]
        
        if to_plus * (plus_cnt+1) >= plus * plus_cnt or to_plus * (plus_cnt+1) + minus >= plus * plus_cnt + (minus + nums[i]):
            plus += nums[i]
            plus_cnt += 1
        else:
            minus += nums[i]

print(plus*plus_cnt + minus)
