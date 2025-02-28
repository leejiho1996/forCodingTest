# 정사각형으로 가리기
import sys
input = sys.stdin.readline

n = int(input())
xMax = -10000
xMin = 10000
yMax = -10000
yMin = 10000

X = []
Y = []

for i in range(n):
    x, y = map(int,input().split())
    X.append(x)
    Y.append(y)
    xMax = max(xMax, x)
    xMin = min(xMin, x)
    yMax = max(yMax, y)
    yMin = min(yMin, y)

dist = max(xMax-xMin, yMax-yMin)

# 제일 하단을 기준으로 만들었을때
check1 = True
for i in range(n):
    if X[i] == xMin or X[i] == xMin+dist or Y[i] == yMin or Y[i] == yMin+dist:
        continue
    else:
        check1 = False
        break 

check2 = True
for i in  range(n):
    if X[i] == xMax or X[i] == xMax-dist or Y[i] == yMax or Y[i] == yMax-dist:
        continue
    else:
        check2 = False
        break

if check1 or check2:
    print(dist)
else:
    print(-1)
