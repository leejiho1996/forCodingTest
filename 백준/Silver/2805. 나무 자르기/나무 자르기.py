# 나무 자르기
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

trees = list(map(int,input().split()))

start = 0
end = max(trees)

while start <= end:
    mid = (start+end)//2

    total = 0
    for i in trees:
        if i - mid > 0:
            total += (i - mid)
    if total >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)
