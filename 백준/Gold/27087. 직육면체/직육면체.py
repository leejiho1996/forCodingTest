# 직육면체
import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    A, B, C, p = map(int,input().split())
    cnt = 0
    
    if A % p == 0:
        cnt += 1

    if B % p == 0:
        cnt += 1

    if C % p == 0:
        cnt += 1

    if cnt >= 2:
        print(1)
    else:
        print(0)
