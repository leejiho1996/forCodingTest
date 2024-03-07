# 나머지 합
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

num = list(map(int,input().split()))

acc = [0]*m
acc[num[0] % m] = 1

s = num[0]

for i in range(1, len(num)):
    s += num[i]
    acc[s%m] += 1

result = 0

for i in range(len(acc)):
    if i == 0:
        for j in range(1, acc[i] + 1):
            result += j
    else:
        for j in range(1, acc[i]):
            result += j

print(result)