# 악덕 사장
import sys
input = sys.stdin.readline

N = int(input())
exp = list(map(int,input().split()))
exp.sort()

for i in range(exp[0], 0, -1):
    if i * N > exp[-1]:
        continue

    check = True
    
    for j in range(N):
        if (j+1) * i > exp[j]:
            check = False
            break

    if check:
        print(i)
        break
