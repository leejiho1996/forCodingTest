# 개미
import sys
input = sys.stdin.readline

w, h = map(int,input().split())
p, q = map(int,input().split())
t = int(input())

x = p + t
y = q + t

if (x // w) % 2 == 0:
    x %= w
else:
    x = w - x % w

if (y // h) % 2 == 0:
    y %= h
else:
    y = h - y % h

print(x, y)
