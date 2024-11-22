# 전구와 스위치
import sys
input = sys.stdin.readline

n = int(input())

start = list(map(int, list(input().rstrip())))
to = list(map(int, list(input().rstrip())))

zero = start.copy()
zero[0] = 1 - zero[0]
zero[1] = 1 - zero[1]
non_zero = start.copy()

zero_cnt = 1
non_cnt = 0

for i in range(1, n):
    if zero[i-1] != to[i-1]:
        if i != n - 1:
            zero[i+1] = 1 - zero[i+1]

        zero[i-1] = 1 - zero[i-1]
        zero[i] =  1 - zero[i]

        zero_cnt += 1

    if non_zero[i-1] != to[i-1]:
        if i != n - 1:
            non_zero[i+1] = 1 - non_zero[i+1]

        non_zero[i-1] = 1 - non_zero[i-1]
        non_zero[i] =  1 - non_zero[i]

        non_cnt += 1

if zero != to:
    zero_cnt = float('inf')

if non_zero != to:
    non_cnt = float('inf')

if min(zero_cnt, non_cnt) == float('inf'):
    print(-1)
else:
    print(min(zero_cnt, non_cnt))
