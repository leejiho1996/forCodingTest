import sys
input = sys.stdin.readline

A, B, N = map(int,input().split())

if A >= B:
    A -= (A // B * B)

A *= 10

for i in range(N):
    if A <= B:
        ret = 0
    else:
        ret = A // B
        A = A - (A // B * B)

    A *= 10

print(ret)
