# 소가 길을 건너간 이유1
import sys
input = sys.stdin.readline

N = int(input())
position = [-1] * 10
result = 0

for i in range(N):
    cow, pos = map(int,input().split())

    if position[cow-1] == -1:
        position[cow-1] = pos
        continue

    if position[cow-1] != pos:
        position[cow-1] = pos
        result += 1

print(result)
