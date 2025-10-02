# 선물
import sys
input = sys.stdin.readline

N, L, W, H = map(int,input().split())
start, end = 0, min(L, W, H)

for _ in range(1000):
    mid = (start + end) / 2
    total = (L // mid) * (W // mid) * (H // mid)
    if total >= N:
        start = mid
    else:
        end = mid

print(end)