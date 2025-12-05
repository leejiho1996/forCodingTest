import sys
input = sys.stdin.readline

N = input().rstrip()

nums = [0] * 10

for i in range(len(N)):
    nums[int(N[i])] += 1

if (nums[6] + nums[9]) % 2 == 0:
    mid = (nums[6] + nums[9]) // 2
else:
    mid = (nums[6] + nums[9]) //2 + 1
    
nums[6] = mid
nums[9] = mid

print(max(nums))