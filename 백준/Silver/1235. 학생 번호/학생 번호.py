# 학생번호
import sys
input = sys.stdin.readline

N = int(input())
nums = []

for i in range(N):
    nums.append(input().rstrip())

L = len(nums[0])

for i in range(1, L+1):
    sett = set()
    for j in range(N):
        cur = nums[j][L-i:]

        if cur in sett:
            break
        else:
            sett.add(cur)

    if len(sett) == N:
        print(i)
        exit()
