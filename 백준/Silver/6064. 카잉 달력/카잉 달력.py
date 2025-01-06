# 카잉 달력
import sys
input = sys.stdin.readline

def gcd(x, y):
    if x < y:
        x, y = y, x

    while y != 0:
        x, y = y, x % y

    return x

t = int(input())

for i in range(t):
    m, n, x, y = map(int,input().split())
    limit = m * n // gcd(m, n)
    year = x
    x %= m
    y %= n
    
    while year <= limit:
        if year % m == x and year % n == y:
            break
        else:
            year += m

    if year <= limit:
        print(year)
    else:
        print(-1)
