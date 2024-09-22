# 수열의 합
import sys
input = sys.stdin.readline

n, l = map(int,input().split())

while l <= 100:
    sub_num = l * (l-1)
    div_num = 2 * l

    resi = (n * 2 - sub_num) % div_num
    quotient = (n * 2 - sub_num) // div_num

    if resi == 0 and quotient >= 0:
        for i in range(quotient, quotient+l):
            print(i, end = " ")
        break
    else:
        l += 1

    if l > 100:
        print(-1)
        break
    
    if quotient <= 0:
        print(-1)
        break