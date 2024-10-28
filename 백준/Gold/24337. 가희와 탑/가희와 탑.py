# 가희와 탑
import sys
input = sys.stdin.readline

n, a, b = map(int,input().split())
buildings = [1] * n
a_cnt = 1
b_cnt = b

if a > b:
    if b == 1:
        buildings[-1] = a
        start = n - a
        end = n
    else:
        end = n - b + 1
        start = end - a 
        b_cnt -= 1
        
elif a == b:
    start = n - (2 * a - 1)
    end = start + a
    b_cnt -= 1
else:
    if a == 1:
        buildings[0] = b
        end = n - b + 1
        b_cnt -= 1
        start = end
    else:
        end = n - b
        start = end - a + 1 
        

for i in range(start, end):
    buildings[i] = a_cnt
    a_cnt += 1

for i in range(end, n):
    buildings[i] = b_cnt
    b_cnt -= 1

if a + b > n + 1:
    print(-1)
else:
    print(*buildings)
