# 피보나치 기념품
import sys
input = sys.stdin.readline

N = int(input())

serim = []
seongju = []

if N == 2:
    for i in range(3):
        print(1)

    print(2)
    exit()

while True:
    if N == 2:
        serim.append(1)
        seongju.append(2)
        break
    
    serim.append(N)
    seongju.append(N-1)
    seongju.append(N-2)

    if N - 3 < 2:
        break
    else:
        N -= 3

print(len(serim))
print(*serim[::-1])
print(len(seongju))
print(*seongju[::-1])
