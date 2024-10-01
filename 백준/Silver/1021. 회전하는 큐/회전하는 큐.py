# 회전하는 큐
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
pick = list(map(int,input().split()))
num = [i for i in range(1, n+1)]

cnt = 0

for i in pick:
    if i == num[0]:
        num = num[1:]
        n -= 1
        continue

    idx = num.index(i)

    if idx <= n - idx:
        cnt += idx
        num = num[idx+1:] + num[0:idx]
    else:
        cnt += n - idx
        num = num[idx+1:] + num[0:idx]

    n -= 1

print(cnt)
    
