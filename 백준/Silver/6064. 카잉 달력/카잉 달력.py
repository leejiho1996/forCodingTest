# 카잉 달력
import sys
input = sys.stdin.readline

def gcd(x, y):
    if x < y:
        x, y = y, x

    if y == 0:
        return x
    
    return gcd(y, x % y)

t = int(input())

for i in range(t):
    m, n, x, y = map(int,input().split())
    limit = m * n // gcd(m, n)
    year = x
    # x == m 이거나 y == n인 경우 0으로 만들어 줘야함
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
