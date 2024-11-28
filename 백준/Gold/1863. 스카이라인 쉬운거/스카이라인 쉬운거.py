# 스카이라인 쉬운거
import sys
input = sys.stdin.readline

n = int(input())

stack = [0]
total = 0

for i in range(n):
    x, y = map(int,input().split())

    while stack and stack[-1] > y:
        total += 1
        stack.pop()

    if stack[-1] < y:
        stack.append(y)

print(total+len(stack)-1)
