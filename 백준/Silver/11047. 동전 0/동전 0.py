# 동전0
import sys
input = sys.stdin.readline

n, k = map(int,input().split())

coin = []
cnt = 0

for i in range(n):
    coin.append(int(input()))

for i in range(n-1, -1,-1):
    if coin[i] > k:
        continue
    else:
        cnt += k // coin[i]
        k -= coin[i] * (k // coin[i])
        

print(cnt)
