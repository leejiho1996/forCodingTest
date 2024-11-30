# 스택 수열
import sys
input = sys.stdin.readline

n = int(input())

cur = 0
stack = []
operation = []
for i in range(n):
    num = int(input())

    if num > cur:
        for j in range(num - cur):
            cur += 1
            operation.append("+")
            stack.append(cur)

    if stack[-1] != num:
        print("NO")
        exit()

    stack.pop()
    operation.append("-")

for i in operation:
    print(i)
    
