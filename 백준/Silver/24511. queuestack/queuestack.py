# 큐스텍
import sys
input = sys.stdin.readline

a = int(input())

b = list(map(int,input().split()))

c = list(map(int,input().split()))

d = int(input())

e = list(map(int,input().split()))


check = []
cnt = 0
for i in range(0, len(b)):
    if b[i] == 0:
        check.append(c[i])

for i in range(len(e)):
    if check:
        print(check.pop(), end = ' ')
    else:
        print(e[cnt], end = ' ')
        cnt += 1
        

         