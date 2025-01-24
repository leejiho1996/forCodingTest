# 집주소
import sys
input = sys.stdin.readline

while True:
    num = input().rstrip()

    if num == "0":
        break
    
    result = 2
    result += len(num) - 1

    for i in num:
        if i == "0":
            result += 4
        elif i == "1":
            result += 2
        else:
            result += 3

    print(result)
