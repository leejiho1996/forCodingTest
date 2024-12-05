import sys
input = sys.stdin.readline

n = int(input())

for i in range(2*n - 1):
    if i >= n:
        print((2*n - i - 1) * "*")
    else:
        print((i+1) * "*")
    