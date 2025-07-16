# 식물 기르기
import sys
input = sys.stdin.readline
import math

N = int(input())
plants = list(map(int,input().split()))

result = 0

for i in plants:
    result += 1/i

print(math.ceil(result))
