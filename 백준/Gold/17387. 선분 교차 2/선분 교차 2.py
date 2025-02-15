import sys
input = sys.stdin.readline

def ccw(a, b, c):
    ab = [b[0] - a[0], b[1] - a[1]]
    ac = [c[0] - a[0], c[1] - a[1]]
    product = ab[0] * ac[1] - ab[1] * ac[0]

    if product > 0:
        return 1  # 반시계 방향
    elif product < 0:
        return -1  # 시계 방향
    else:
        return 0  # 일직선

def is_intersect(a, b, c, d):
    AB = ccw(a, b, c) * ccw(a, b, d)
    CD = ccw(c, d, a) * ccw(c, d, b)

    if AB == 0 and CD == 0:
        # 두 선분이 일직선상에 있을 경우, 겹치는지 확인
        return max(a, c) <= min(b, d)  # x, y 기준 비교
    return AB <= 0 and CD <= 0

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

# A, B 정렬
A = (x1, y1)
B = (x2, y2)
C = (x3, y3)
D = (x4, y4)

if A > B: A, B = B, A
if C > D: C, D = D, C

print(1 if is_intersect(A, B, C, D) else 0)
