# 10828 스택
import sys
input = sys.stdin.readline

n = int(input())

stack = []
for i in range(n):
    c = input().rstrip()
    command = c.split(' ')

    if command[0] == "push":
        stack.append(command[1])
    elif command[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif command[0] == "size":
        print(len(stack))
    else:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
