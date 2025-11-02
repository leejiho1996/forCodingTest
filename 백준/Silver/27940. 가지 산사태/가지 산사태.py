# 가지 산사태
import sys
input = sys.stdin.readline

N, M, K = map(int,input().split())

total = 0

for i in range(M):
    t, r = map(int,input().split())
    total += r

    if total > K:
        print(i+1, 1)
        exit()

print(-1)
    