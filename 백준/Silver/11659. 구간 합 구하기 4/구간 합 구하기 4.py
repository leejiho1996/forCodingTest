# 구간 합 구하기4
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

num = list(map(int,input().split()))

summ = 0
num2 = []

for i in num:
    summ += i
    num2.append(summ)

for i in range(m):
    start, end = map(int,input().split())
    if start == 1:
        print(num2[end-1])
    else:
        print(num2[end-1] - num2[start-2])