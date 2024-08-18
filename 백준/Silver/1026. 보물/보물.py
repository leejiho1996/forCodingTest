import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort(reverse=True)
b.sort()

total = 0
for i in range(n):
    total += a[i] * b[i]

print(total)