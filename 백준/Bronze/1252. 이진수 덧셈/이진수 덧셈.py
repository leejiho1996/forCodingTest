import sys
input = sys.stdin.readline

a, b = input().rstrip().split()
a = int(a, 2)
b = int(b, 2)
c = a + b
result = []

while c >= 2:
    result.append(c%2)
    c //= 2

result.append(c)
print(*result[::-1], sep="")