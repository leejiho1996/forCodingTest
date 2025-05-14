# 등차수열의 합
import sys
input = sys.stdin.readline

dic = {2:(2, 1), 3:(3, 3), 4:(4, 6), 5:(5, 10)}

l = int(input())
r = int(input())
k = int(input())

x, d = dic[k]

if d % x == 0:
    left = max(1, l-d-1)
    right = max(1, r-d)
    print(right//x - left//x)
else:
    left1 = max(1, l-d-1)
    right1 = max(1, r-d)
    left2 = max(1, l-2*d-1)
    right2 = max(1, r-2*d)

    print((right1//x-left1//x) + (right2//x-left2//x))
