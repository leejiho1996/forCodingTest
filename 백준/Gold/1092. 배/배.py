# 배
import sys
input = sys.stdin.readline

N = int(input())
crane = list(map(int,input().split()))

M = int(input())
pears = list(map(int,input().split()))

crane.sort(reverse = True)
pears.sort(reverse = True)

cnt = 0
time = 0

if crane[0] < pears[0]:
    print(-1)
    exit()

while pears:
    for i in range(N):
        cur = crane[i]
        if pears and cur < pears[-1]:
                break
        for v in pears:
            if v <= cur:
                pears.remove(v)
                break
    time += 1
    
print(time)
