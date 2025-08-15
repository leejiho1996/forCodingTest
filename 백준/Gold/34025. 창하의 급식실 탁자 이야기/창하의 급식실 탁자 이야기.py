# 창하의 급식실 탁자 이야기
import sys
input = sys.stdin.readline

N = int(input())
result = 0

odd = []
even = []
one = 0

for i in range(N):
    num = int(input())

    if num == 1:
        result += 1 
    elif num % 2 == 1:
        odd.append(num)
    else:
        even.append(num)

if result:
    cnt = 0

    while odd and cnt < 2:
        result += odd.pop() // 2 + 1
        cnt += 1
    
while odd:
    cur = odd.pop()

    if result:
        result += 1
        
    result += cur // 2 + 1
    
    if odd:
        result += odd.pop() // 2 + 1

for i in even:
    if result:
        result += 1
        
    result += i // 2

print(result)
