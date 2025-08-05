# donstructive
import sys
input = sys.stdin.readline

N = int(input())
result = [0] * N

num = N
left = N // 2 - 1
right = N // 2

if N % 2 == 1:
    result[N // 2] = N
    num -= 1
    right += 1

while left >= 0 and right < N:
    result[right] = num
    result[left] = num - 1

    right += 1
    left -= 1
    
    num -= 2

print(*result)
