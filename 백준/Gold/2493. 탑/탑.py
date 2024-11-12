import sys
input = sys.stdin.readline

n = int(input())
towers = list(map(int,input().split()))
stack = []
result = [0] * n

for i in range(n):
    num = towers[i]
    while stack:
        if towers[stack[-1]] > num:
            result[i] = stack[-1] + 1
            break
        else:
            stack.pop()

    stack.append(i)

print(*result)
