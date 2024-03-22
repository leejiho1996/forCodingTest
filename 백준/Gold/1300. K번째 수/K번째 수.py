# K번째 수
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

start = 1
end = n*n

while start <= end:
    mid = (start + end) // 2
    total = 0

    for i in range(1, n+1):
        if mid // i > n:
            total += n
        else:
            total += mid//i

    if total >= k:
        end = mid - 1
    else:
        start = mid + 1

print(end + 1)
        