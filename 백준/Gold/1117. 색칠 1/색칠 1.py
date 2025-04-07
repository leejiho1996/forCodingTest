# 색칠1
import sys
input = sys.stdin.readline

W, H, f, c, x1, y1, x2, y2 = map(int,input().split())

if f > W // 2:
    f_end = W - f
else:
    f_end = f

total = W * H
colored = (x2 - x1) * (y2 - y1)

if x1 >= f_end:
    f_wrapped = 0
elif x1 < f_end < x2:
    f_wrapped = (f_end - x1) * (y2 - y1)
else:
    f_wrapped = colored

c += 1

result = total - (f_wrapped * c * 2 + (colored - f_wrapped) * c)

print(result)
