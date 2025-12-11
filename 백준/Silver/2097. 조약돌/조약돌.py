# 조약돌
import sys
input = sys.stdin.readline

N = int(input())
rt = int(N**(0.5))
sq = rt**2

if N <= 4:
    print(4)
    exit()
    
w = rt-1
h = rt-1

if (N-sq) // rt:
    w += (N-sq) // rt

if (N-sq) % rt:
    w += 1

print((w+h) * 2)
