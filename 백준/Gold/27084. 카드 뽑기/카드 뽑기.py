# 카드뽑기
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().split()))
DIV = 1_000_000_000 + 7
result = 1

count = [1] * (N+1)

for i in nums:
    count[i] += 1

for i in range(1, N+1):

    if count[i] == 0:
        continue
    else:
        result *= count[i]
        result %= DIV

print(result - 1)
