# 반올림

import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    num = int(input())
    length = len(str(num))

    for j in range(1, length):
        resi = num % (10**j)
        if resi // 10**(j-1)>= 5:
            num += 10**j
            num -= resi
        else:
            num -= resi
        
    print(num)
