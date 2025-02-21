# 수 나누기 게임
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
maxNum = max(nums)
score = [0] * (maxNum+1)
present = [0] * (maxNum+1)

for i in range(n):
    present[nums[i]] = 1

for i in range(n):
    num = nums[i]
    for j in range(num*2, maxNum+1, num):
        score[j] -= 1

        if present[j]:
            score[num] += 1

for i in range(n):
    print(score[nums[i]], end = " ")
