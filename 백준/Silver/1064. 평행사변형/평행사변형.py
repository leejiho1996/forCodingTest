# 평행사변형
import sys
input = sys.stdin.readline

def getLength(x1, y1, x2, y2):

    return ((x1-x2)**2 + (y1-y2)**2)**(0.5)

x1, y1, x2, y2, x3, y3 = map(int,input().split())

if (x2-x1)*(y3-y1) - (x3-x1)*(y2-y1) == 0:
    print(-1)
    exit()

result = []

result.append(getLength(x1, y1, x2, y2))
result.append(getLength(x1, y1, x3, y3))
result.append(getLength(x2, y2, x3, y3))

minn = 1000000
maxx = 0

for i in range(3):
    for j in range(i+1, 3):
        cur = (result[i] + result[j]) * 2
        minn = min(cur, minn)
        maxx = max(cur, maxx)

print(maxx - minn)
