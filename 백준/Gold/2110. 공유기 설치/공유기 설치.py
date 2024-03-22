# 공유기 설치
import sys
input = sys.stdin.readline

n, c = map(int,input().split())

house = [int(input()) for _ in range(n)]
house.sort()

if c == 2:
    print(house[n-1] - house[0])
    exit()

start = 1
end = house[n-1] - house[0]

while start <= end:
    mid = (start + end) // 2
    now = house[0]

    cnt = 1

    for i in range(1, n):
        if house[i] - now >= mid:
            cnt += 1
            now = house[i]

    if cnt >= c:
        start = mid + 1
    else:
        end = mid - 1

print(start-1)