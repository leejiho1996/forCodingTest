import sys
input = sys.stdin.readline

check = "0123456789"
a = int(input())
b = int(input())
c = int(input())

mul = str(a * b * c)

for i in check:
    print(mul.count(i))
