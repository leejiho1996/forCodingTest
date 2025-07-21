# 사람의 수
import sys
input = sys.stdin.readline

N = int(input())
scores = []

for i in range(N):
    integer, floating = input().rstrip().split(".")
    scores.append(int(integer) * 1000 + int(floating))

for i in range(1, 1001):
    cnt = 0
    for j in range(N):
        cur = scores[j]

        start = 1
        end = i * 10

        while start <= end:

            mid = (start + end) // 2

            if int(mid / i * 1000) <= cur:
                start = mid + 1
            else:
                end = mid - 1

        if int((start - 1) / i * 1000) == cur:
            cnt += 1

    if cnt == N:
        break

print(i)
            
