# 하늘에서 떨어지는 무한개의 별
import sys
input = sys.stdin.readline

def calGCD(a, b):

    while b > 0:
        a, b = b, a % b

    return a
    
s0, X, M, D, K = map(int,input().split())
D -= 1

if M == 1:
    print(0)
    exit()

gcd = calGCD(X, M)
maxx = s0 + ((M - s0 - 1) // gcd) * gcd

if maxx == 0:
    print(0)
    exit()

term = K // maxx

print(D // term)
