# 줄어드는 수
import sys
input = sys.stdin.readline

def backtrack(n, last):
    nums.append(n)

    for i in range(0, last):
        backtrack(n*10+i, i)

N = int(input())
nums = []

for i in range(0, 10):
    backtrack(i, i)

if N > len(nums):
    print(-1)
else:
    nums.sort()
    print(nums[N-1])
