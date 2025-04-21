# Cow Race
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
result = 0

Bessie = [0]
for i in range(N):
    speed, time = map(int,input().split())

    for j in range(time):
        Bessie.append(Bessie[-1] + speed)

Elsie = [0]
for i in range(M):
    speed, time = map(int,input().split())

    for j in range(time):
        Elsie.append(Elsie[-1]+speed)

cur = 0
for i in range(len(Bessie)):
    if cur == 0:
        if Bessie[i] > Elsie[i]:
            cur = 1
        elif Bessie[i] < Elsie[i]:
            cur = -1
            
    if Bessie[i] > Elsie[i] and cur == -1:
        cur = 1
        result += 1
    elif Bessie[i] < Elsie[i] and cur == 1:
        cur =-1
        result += 1

print(result)
