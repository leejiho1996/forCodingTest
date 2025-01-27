# 삼각형의 최단 경로
import sys
import math
input = sys.stdin.readline

start, end = map(int,input().split())

if start > end:
    start, end = end, start

startLevel = math.ceil(start**(0.5))
endLevel = math.ceil(end**(0.5))    
num = start # 레벨 이동이 끝난 후 제일 왼쪽의 숫자
pos = 0 # 레벨 이동이 끝난 후 가능한 숫자의 갯수

if start % 2 == startLevel % 2:
    move = - 1
    num += 1
else:
    move = 0
    pos += 1

move += (endLevel - startLevel) * 2
levelMove = startLevel * 2 - 1

while startLevel < endLevel:
    num += levelMove
    levelMove += 2
    startLevel += 1
    pos += 1

minn = abs(num - end)
for i in range(1, pos):
    minn = min(minn, abs((i*2 + num) - end))

print(move + minn)