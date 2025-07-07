# 뉴턴과 사과
import sys
input = sys.stdin.readline

people = list(map(int,input().split()))
x, y, r = map(int,input().split())

h, l = x + r, x - r

for i in range(4):
    if people[i] == x:
        print(i+1)
        exit()

print(0)

