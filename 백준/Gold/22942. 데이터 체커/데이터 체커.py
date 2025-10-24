# 데이터 체커
import sys
input = sys.stdin.readline

N = int(input())
points = []

for i in range(N):
    x, r = map(int,input().split())
    points.append((x+r, i))
    points.append((x-r, i))

points.sort()

stack = []

for i in range(2*N):

    if stack and stack[-1] == points[i][1]:
        stack.pop()
    else:
        stack.append(points[i][1])

if stack:
    print("NO")
else:
    print("YES")
