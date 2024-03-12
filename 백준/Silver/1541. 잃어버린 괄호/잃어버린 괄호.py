# 잃어버린 괄호
import sys
input = sys.stdin.readline

a = input().rstrip()
expression = a.split('-')


summ = 0
check = False

for i in expression:
    if "+" in i:
        s = 0
        for j in i.split("+"):
            s += int(j)
        if check == False:
            summ += s
            check = True
        else:
            summ -= s
    else:
        if check == False:
            summ += int(i)
            check = True
        else:
            summ -= int(i)

print(summ)
