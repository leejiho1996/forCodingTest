# 탑
import sys
input = sys.stdin.readline

n = int(input())
towers = list(map(int,input().split()))
MAX = 100000001
towers += [MAX]
result = [0] * (n+2)

stack = [(0, MAX), (1, towers[0])]

for i in range(1, n+1):
    if towers[i] > stack[-1][1]:
        while stack and stack[-1][1] < towers[i]:
            idx, num = stack.pop()
            result[idx] = stack[-1][0]

    stack.append((i+1, towers[i]))

print(*result[1:n+1])
