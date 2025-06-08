# 저울
import sys
input = sys.stdin.readline

N = int(input())
weights = list(map(int,input().split()))

weights.sort()

minn = 1

for i in range(N):

    if minn < weights[i]:
        break

    minn += weights[i]

print(minn)
     
