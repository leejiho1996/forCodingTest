# 간단한 순열 문제
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().split()))
result = 0

stack = []

for i in range(N):

    while stack and stack[-1] < nums[i]:

        stack.pop()
        result += 1

        if stack:
            result += 1

    stack.append(nums[i])

result += len(stack) - 1

print(result)
