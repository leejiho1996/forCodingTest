# 생일
import sys
input = sys.stdin.readline

N = int(input())

lists = []

for i in range(N):
    name, day, month, year = input().rstrip().split()

    lists.append((int(year), int(month), int(day), name))

lists.sort(reverse = True)

print(lists[0][-1])
print(lists[-1][-1])
