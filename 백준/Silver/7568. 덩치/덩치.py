# 덩치 7568
import sys
input = sys.stdin.readline

n = int(input())
people = []
result = [0] * n

for i in range(n):
    w, h = map(int,input().split())
    people.append((w, h))

for i in range(n):
    w, h = people[i]
    cnt = 1
    for j in range(n):
        if i == j:
            continue
        ow, oh = people[j]
        if ow > w and oh > h:
            cnt += 1
    result[i] = cnt
         

print(*result)
