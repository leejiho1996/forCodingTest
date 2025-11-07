# 머리 톡톡
import sys
input = sys.stdin.readline

N = int(input())
cnt = [0] * 1000001
nums = [0] * N

for i in range(N):
    num = int(input())
    nums[i] = num
    cnt[num] += 1
    
for i in range(N):
    cur = nums[i]
    result = -1
        
    for j in range(1, int(cur**(0.5))+1):

        if cur % j == 0:
            result += cnt[j]

            if j != cur//j:
                result += cnt[cur//j]

    print(result)
