# 터렛
import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())

    distance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5

    if distance > r1 + r2:
        print(0)

    elif x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)

    elif distance < r1 + r2 and (distance == (r1-r2) or distance == (r2-r1)):
        print(1)

    elif distance == r1 + r2:
        print(1)

    elif distance < abs(r1 - r2):
        print(0)

    elif distance < r1 + r2:
        print(2)
        
