# 악덕 사장
import sys
input = sys.stdin.readline

N = int(input())
exp = list(map(int,input().split()))
exp.sort()
result = 1_000_000_000

for i in range(N):
    result = min(result, exp[i] // (i+1))

print(result)
