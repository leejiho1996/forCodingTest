# SW 수열 구하기
import sys
input = sys.stdin.readline

N = int(input())
result = [0] * N

idx = 0
small = 1
big = N

while idx < N:

    if idx % 2 == 0:
        result[idx] = small
        small += 1
    else:
        result[idx] = big
        big -= 1

    idx += 1

print(*result)
    
