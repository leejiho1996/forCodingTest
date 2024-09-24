# 수열 정렬
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))

sorted_a = sorted(a)

dic = {}
for i in range(n):
    num = sorted_a[i]

    if num not in dic:
        dic[num] = i

result = []

for i in a:
    result.append(dic[i])
    dic[i] += 1

print(*result)
