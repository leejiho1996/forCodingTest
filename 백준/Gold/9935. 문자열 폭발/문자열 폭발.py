# 문자열 폭발
import sys
input = sys.stdin.readline

string = list(input().rstrip())
string = string[::-1]

check = list(input().rstrip())

lenn = len(check)
stack = []


while string:
    c = string.pop()
    stack.append(c)
    while len(stack) >= lenn and stack[len(stack)-lenn:] == check:
        for i in range(lenn):
            stack.pop()

if len(stack) == 0:
    print("FRULA")
else:
    print(*stack, sep='')