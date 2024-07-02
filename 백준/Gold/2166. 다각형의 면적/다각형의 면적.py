# 다각형의 면적
import sys
input = sys.stdin.readline

n = int(input())
point = []

for i in range(n):
    point.append(tuple(map(int,input().split())))

area = 0
for i in range(n):
    x1, y1 = point[i]
    x2, y2 = point[(i+1) % n]
    area += x1 * y2
    area -= y1 * x2

area = abs(area)/2

print(f'{area:.1f}')
