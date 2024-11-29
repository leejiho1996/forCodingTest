# ACM 호텔
import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    h, w, n = map(int,input().split())
    col = 1 + ((n-1) // h)
    floor = 100 * ((n-1) % h + 1)
    print(floor + col)
