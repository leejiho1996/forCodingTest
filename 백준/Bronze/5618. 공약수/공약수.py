from math import gcd, sqrt

def div(n: int) -> list:

    tmp = []
    for i in range(1, int(sqrt(n)) + 1):
        if (n % i == 0):
            tmp.append(i) 
            if ( (i**2) != n) : 
                tmp.append(n // i)
    tmp.sort()
    return tmp

n = int(input())
if n == 2:
    a, b = map(int, input().split())
    ls = div(gcd(a, b))
    for element in ls:
        print(element)
else:
    a, b, c = map(int, input().split())
    ls = div(gcd(a, gcd(b, c)))
    for element in ls:
        print(element)