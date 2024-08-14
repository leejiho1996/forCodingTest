from sys import stdin
from math import gcd, lcm

for _ in range(int(stdin.readline())):
    a, b = map(int, stdin.readline().split())
    print(lcm(a, b), gcd(a, b))