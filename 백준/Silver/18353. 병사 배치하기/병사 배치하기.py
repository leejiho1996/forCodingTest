# 병사 배치하기
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().split()))
lis = [-nums[0]]

for i in range(1, N):
    cur = -nums[i]

    if cur > lis[-1]:
        lis.append(cur)
        continue

    start = 0
    end = len(lis)-1

    while start <= end:

        mid = (start + end) // 2

        if lis[mid] >= cur:
            end = mid - 1
        else:
            start = mid + 1

    lis[end+1] = cur
        
print(N - len(lis))
        
        
