# 짐 챙기는 숌
import sys
input = sys.stdin.readline

N, M = map(int,input().split())

if N == 0:
    print(0)
    exit()

books = list(map(int,input().split()))

cnt = 1
cur = 0

for i in range(N):
    if cur + books[i] > M:
        cur = books[i]
        cnt += 1
    else:
        cur += books[i]

print(cnt)

