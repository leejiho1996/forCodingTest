# GCD(n,k) = 1
import sys
input = sys.stdin.readline

n = int(input())
result = n

for i in range(2, int(n**(0.5))+1):
    if n % i == 0:
        result = result - result // i
        while n % i == 0:
            n //= i

if n > 1:
    result = result - result // n

print(result)
