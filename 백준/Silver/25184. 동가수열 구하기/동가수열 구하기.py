# 등가 수열 구하기
import sys
input = sys.stdin.readline

N = int(input())

result = [0] * N

s = N//2
e = N
idx = 0

if N % 2:
    result[0] = e
    e -= 1
    idx += 1

while e > N//2:
    result[idx] = s
    result[idx+1] = e

    s -= 1
    e -= 1

    idx += 2

print(*result)
