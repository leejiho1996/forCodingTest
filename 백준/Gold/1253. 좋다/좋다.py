# 좋다
import sys
input = sys.stdin.readline

n = int(input())

num = list(map(int,input().split()))
num.sort()

good = 0

for i in range(len(num)):

    number = num[i]
    left = 0
    right = n-2

    part = num[:i] + num[i+1:]

    while left < right:
        if part[left] + part[right] < number:
            left += 1

        elif part[left] + part[right] > number:
            right -= 1

        else:
            good += 1
            break
    
print(good)
