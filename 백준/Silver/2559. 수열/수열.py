#수열
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

num = list(map(int,input().split()))

summ = 0
maxx = -100_000_000

num2 = [0]

for i in num:
    summ += i
    num2.append(summ)

for i in range(m, n+1):
    maxx = max(maxx, num2[i] - num2[i-m])


print(maxx)