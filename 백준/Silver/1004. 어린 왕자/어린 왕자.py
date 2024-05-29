# 어린 왕자
import sys
input = sys.stdin.readline

t = int(input())

def incircle(x, y, c_x, c_y, r):
    if (x-c_x)**2 + (y-c_y)**2 < r**2:
        return True
    else:
        return False

for i in range(t):
    x1, y1, x2, y2 = map(int,input().split())

    n = int(input())
    cnt = 0
    
    for j in range(n):
        cx, cy, r = map(int,input().split())
        if incircle(x1, y1, cx, cy, r) and not incircle(x2, y2, cx, cy, r):
            cnt += 1
        elif not incircle(x1, y1, cx, cy, r) and incircle(x2, y2, cx, cy, r):
            cnt += 1

    print(cnt)
        
