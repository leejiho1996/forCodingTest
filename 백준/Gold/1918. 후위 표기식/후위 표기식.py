# 후위 표기식
import sys
input = sys.stdin.readline

pre = input().rstrip() # 중위표기식
post = [] # 후위표기식
priority = {"+": 0, "-": 0, "*": 1, "/": 1} # 기본 연산자 우선순위
bracket = 0 # 앞에 나온 괄호 갯수
stack = []

for char in pre:
    if char == "(":
        bracket += 1
    elif char == ")":
        bracket -= 1
    elif char not in priority:
        post.append(char)
    else:
        while stack and stack[-1][1] >= priority[char] + bracket*2:
            post.append(stack.pop()[0])
            
        stack.append((char, priority[char] + bracket*2))

while stack:
    post.append(stack.pop()[0])

print(*post, sep="")
