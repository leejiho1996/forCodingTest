# 3차원 막대기 연결하기
import sys
input = sys.stdin.readline

X1, Y1, Z1, X2, Y2, Z2 = map(int,input().split())
N = int(input())
sticks = list(map(int,input().split()))
sticks.sort(reverse=True)

dist = ((X2 - X1)**2+(Y2 - Y1)**2+(Z2 - Z1)**2)**(0.5)

if sum(sticks) >= dist:
    if sticks[0] - sum(sticks[1:]) <= dist:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
