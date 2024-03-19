# 괄호

import sys; input = sys.stdin.readline

a = int(input())

for i in range(a):
    stack = []
    b = list(input().strip())
    for j in b:
        if not stack and j == ')':
            stack.append(1)
            break
        elif j == '(':
            stack.append(j)
        else:
            stack.pop()
    
    if stack:
        print('NO')
    else:
        print('YES')