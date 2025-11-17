# 한 줄로 서기
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().split()))

result = []

for i in range(N-1, -1, -1):
    result.insert(nums[i], i+1)
        
print(*result)