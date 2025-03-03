# 선분 교차2
import sys
input = sys.stdin.readline

def ccw(a, b, c):
    ab = [b[0] - a[0], b[1] - a[1]]
    ac = [c[0] - a[0], c[1] - a[1]]

    product = ab[0] * ac[1] - ab[1] * ac[0]

    if product < 0:
        return -1
    elif product > 0:
        return 1
    else:
        return 0

        
x1, y1, x2, y2 = map(int,input().split())
x3, y3, x4, y4 = map(int,input().split())

A = (x1, y1)
B = (x2, y2)
C = (x3, y3)
D = (x4, y4)

if B < A: # A < B가 되도록 만들어준다
    A, B = B, A

if D < C: # C < D가 되도록 만들어준다
    C, D = D, C

AB = ccw(A, B, C) * ccw(A, B, D)
CD = ccw(C, D, A) * ccw(C, D, B)

if AB <= 0 and CD <= 0: # 서로 교차하는 경우
    print(1)
else: # 교차하지 않는 경우
    print(0)
            
