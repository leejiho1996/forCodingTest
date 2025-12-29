# 수들의 합
import sys
input = sys.stdin.readline

N = int(input())

s = 1
ret = 0
cnt = 0

while ret < N:

    ret += s
    s += 1

    if ret > N:
        break

    cnt += 1

print(cnt)
