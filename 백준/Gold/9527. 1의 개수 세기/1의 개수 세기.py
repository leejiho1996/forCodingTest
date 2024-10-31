# 1의 개수 세기
import sys
input = sys.stdin.readline

a, b = map(int,input().split())

start = 1
a_cnt = 0
b_cnt = 0

head = a - 1

def cal(number):
    start = 1
    cnt = 0
    
    while start <= number:
        num = number - (start - 1)
        quo = num // start
        resi = num % start

        cnt += (quo+1) // 2 * start

        if quo % 2 == 0:
            cnt += resi
            
        start *= 2

    return cnt

print(cal(b) - cal(a-1))
    
