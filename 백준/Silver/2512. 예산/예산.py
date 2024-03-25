# 예산
import sys
input = sys.stdin.readline

n = int(input())

num = list(map(int,input().split()))
m = int(input())

start = 1
end = max(num)

while start <= end:
    mid = (start + end)//2

    total = 0
    for i in num:
        if i <= mid:
            total += i
        else:
            total+= mid
    if m >= total:
        start = mid + 1
    else:
        end = mid - 1

print(start-1)