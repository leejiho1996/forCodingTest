# 점숫자
import sys
input = sys.stdin.readline

T = int(input())
head = [1,1]
start = [0] * 10001
dic = {}
s = 1
e = 1
add = 1

for i in range(1, 10001):
    start[i] = s
    dic[head[-1]] = i
    head.append(head[-1] + i)

    if i == e:
        s += add
        add += 1
        e += add
        
for i in range(T):
    a, b = map(int,input().split())

    ax = 1 + a - start[a]
    bx = 1 + b - start[b]
    ay = dic[start[a]] - (ax-1)
    by = dic[start[b]] - (bx-1)

    print(head[ax+bx+ay+by-1] + ax+bx-1)
