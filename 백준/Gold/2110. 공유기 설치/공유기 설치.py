# 공유기 설치
import sys
input = sys.stdin.readline

n, c = map(int,input().split())

house = [int(input()) for _ in range(n)]
house.sort()

if c == 2:
    print(house[n-1] - house[0])
    exit()

start = 1 # 최소거리 1
end = house[n-1] - house[0] # 최대거리

while start <= end:
    mid = (start + end) // 2
    now = house[0]

    cnt = 1

    for i in range(1, n):
        if house[i] - now >= mid:
            cnt += 1
            now = house[i]

    # Lowerbound로는 풀 수 없다. ex) 거리가 2 인경우에도 cnt는 3 이나옴
    # UpperBound를 구하고 -1 해서 구해야한다.
    if cnt >= c:
        start = mid + 1
    else:
        end = mid - 1

print(start-1)