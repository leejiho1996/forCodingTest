# 곱셈 (분할정복)
import sys
input = sys.stdin.readline

def divide(a, b):
    if b == 1:
        return a % c

    result = divide(a , b//2)

    if b % 2 == 1:
        return result * result * a % c
    else:
        return result * result % c

a, b, c = map(int,input().split())

print(divide(a,b))