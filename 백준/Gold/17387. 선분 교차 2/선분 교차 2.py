# 선분 교차2
import sys
input = sys.stdin.readline

def ccw(a, b, c):
    ab = [b[0] - a[0], b[1] - a[1]]
    ac = [c[0] - a[0], c[1] - a[1]]

    product = ab[0] * ac[1] - ab[1] * ac[0]

    return product

def sortVector(x1, y1, x2, y2):
    
    if x2 < x1:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    elif x1 == x2 and y2 < y1:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    return [x1, y1, x2, y2]

        
x1, y1, x2, y2 = map(int,input().split())
x3, y3, x4, y4 = map(int,input().split())

sortAB = sortVector(x1, y1, x2, y2)
sortCD = sortVector(x3, y3, x4, y4)

A = sortAB[:2]
B = sortAB[2:]
C = sortCD[:2]
D = sortCD[2:]

AB = ccw(A, B, C) * ccw(A, B, D)
CD = ccw(C, D, A) * ccw(C, D, B)

if AB <= 0 and CD <= 0:
        
    if AB == 0 and CD == 0:
        if not(B < C or D < A):
            print(1)
        else:
            print(0)
    else:
        print(1)
else:
    print(0)
            
