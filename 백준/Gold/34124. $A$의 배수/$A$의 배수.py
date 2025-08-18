# A의 배수
import sys
input = sys.stdin.readline

Q = int(input())

for i in range(Q):
    N, A = map(int,input().split())

    if N % 2 == 1:
        print("O")
    else:
        if N == 2 and A == 2:
            print("O")
        else:
            print("I")