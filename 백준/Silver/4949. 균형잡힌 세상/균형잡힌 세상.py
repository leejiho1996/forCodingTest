# 균형잡힌 세상

import sys; input = sys.stdin.readline

while True:
    s = []
    b = input()
    if b[0] == '.':
        break
    for j in b:
        if j == ')':
            if not s:
                s.append(1)
                break
            elif s[-1] != '(':
                s.append(1)
                break
            else:
                s.pop()
        elif  j ==']':
            if not s:
                s.append(1)
                break
            elif s[-1] != '[':
                s.append(1)
                break
            else:
                s.pop()
        elif j == '(':
            s.append(j)
        elif j == '[':
            s.append(j)
        
    if s:
        print('no')
    else:
        print('yes')