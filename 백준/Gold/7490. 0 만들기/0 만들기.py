# 0만들기
import sys
input = sys.stdin.readline

def parse(expr):
    expr = expr.replace(" ", "")
    numbers = []
    op = []
    
    num = ""
    for i in range(len(expr)):
        if expr[i] == "+" or expr[i] == "-":
            op.append(expr[i])
            numbers.append(int(num))
            num = ""
        else:
            num += expr[i]

    if len(num) > 0:
        numbers.append(int(num))

    cur = 1
    total = numbers[0]

    for i in op:
        if i == "+":
            total += numbers[cur]
        else:
            total -= numbers[cur]
        cur += 1
    
    return total

def dfs(expr, num, cnt):
    oper = ("+", "-", " ")
    
    if cnt == len(num):
        if parse(expr) == 0:
            result.append(expr)
        return

    if cnt == len(num):
        return
    
    for i in oper:
        dfs(expr+i+num[cnt], num, cnt+1)

t = int(input())

for i in range(t):
    num = int(input())
    word = ""
    result = []
    
    for j in range(1, num+1):
        word += str(j)

    dfs(word[0], word, 1)
    result.sort()
    
    for i in result:
        print(i)
    print()
    
