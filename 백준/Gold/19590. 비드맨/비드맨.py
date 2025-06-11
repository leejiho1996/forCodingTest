# 비드맨
import sys
input = sys.stdin.readline

N = int(input())
beeds = []
total = 0

for i in range(N):
    beed = int(input())
    beeds.append(beed)
    total += beed

beeds.sort()

if beeds[-1] > total - beeds[-1]:
    print(beeds[-1] - (total - beeds[-1]))
else:
    if sum(beeds) % 2:
        print(1)
    else:
        print(0)
