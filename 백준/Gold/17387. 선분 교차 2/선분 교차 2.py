import sys
input = sys.stdin.readline

def ccw(a, b, c):
    """ 세 점 (a, b, c)에 대한 CCW 연산을 수행하여 방향성을 반환하는 함수 """
    product = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    if product > 0:
        return 1  # 반시계 방향
    elif product < 0:
        return -1  # 시계 방향
    else:
        return 0  # 일직선

def isIntersect(x1, y1, x2, y2, x3, y3, x4, y4):
    A, B = (x1, y1), (x2, y2)
    C, D = (x3, y3), (x4, y4)

    # CCW 계산
    AB_C = ccw(A, B, C)
    AB_D = ccw(A, B, D)
    CD_A = ccw(C, D, A)
    CD_B = ccw(C, D, B)

    # 두 선분이 일반적인 교차를 이루는 경우
    if AB_C * AB_D <= 0 and CD_A * CD_B <= 0:
        # 일직선상에 있는 경우, 겹치는지 추가 확인
        if AB_C == 0 and AB_D == 0 and CD_A == 0 and CD_B == 0:
            return (min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and
                    min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2))
        return True
    return False

# 입력 받기
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

# 결과 출력
print(1 if isIntersect(x1, y1, x2, y2, x3, y3, x4, y4) else 0)
