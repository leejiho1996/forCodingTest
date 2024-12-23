# 패션왕 신해빈
import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    dic = {}
    n = int(input())
    for j in range(n):
        c, t = input().rstrip().split()

        if t in dic:
            dic[t] += 1
        else:
            dic[t] = 1

    result = 1
    for j in dic.keys():
        result *= dic[j] + 1

    print(result - 1)
    