# 선분 그룹
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

def find(n):
    if parent[n] != n:
        parent[n] = find(parent[n])

    return parent[n]

def isGroup(i, j):
    p1 = find(i)
    p2 = find(j)

    if p1 != p2:
        parent[p1] = p2
        groupCnt[p2] += groupCnt[p1]
        groupCnt[p1] = 0

n = int(input())
lines = []
parent = [i for i in range(n)]
groupCnt = [1 for _ in range(n)]

groups = 0
maxGroup = 0

for i in range(n):
    lines.append(list(map(int,input().split())))

for i in range(n):
    x1, y1, x2, y2 = lines[i]
    A = [x1, y1]
    B = [x2, y2]

    if B < A:
        A, B = B, A
    for j in range(i+1, n):
        

        x3, y3, x4, y4 = lines[j]
        C = [x3, y3]
        D = [x4, y4]

        if D < C:
            C, D = D, C

        AB = ccw(A, B, C) * ccw(A, B, D)
        CD = ccw(C, D, A) * ccw(C, D, B)
    
        if AB == 0 and CD == 0: # 같은 직선상에 있는 경우
            if not(B < C or D < A):
                isGroup(i, j)
        elif AB <= 0 and CD <= 0:            
            isGroup(i, j)

for i in range(n):
    if groupCnt[i] != 0:
        groups += 1
        maxGroup = max(maxGroup, groupCnt[i])

print(groups)
print(maxGroup)
