import sys
input = sys.stdin.readline

a, b = map(int,input().split())
a -= 1
b -= 1
ar = a % 4
ac = a // 4
br = b % 4
bc = b // 4
print(abs(ar - br) + abs(ac - bc))