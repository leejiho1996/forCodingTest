# 다이어트
import sys
input = sys.stdin.readline

G = int(input())

check = False

for i in range(1, G+1):
    cur = i**2 + G

    if cur**(0.5) == int(cur**(0.5)):
        check = True
        print(int(cur**(0.5)))

if not check:
    print(-1)
