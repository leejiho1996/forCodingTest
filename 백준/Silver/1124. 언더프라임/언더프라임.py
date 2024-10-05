# 언더프라임
import sys
input = sys.stdin.readline

a, b = map(int,input().split())

prime = [0] * 18
prime[0] = 1
prime[1] = 1

for i in range(2, 18):
    num = i
    if prime[num] == 0:
        cnt = 2
        while num*cnt < 18:
            prime[num*cnt] = 1
            cnt += 1
            
def factorization(num):
    prime_cnt = 0
    divide = 2

    while divide <= num**(1/2):
        if num % divide == 0:
            prime_cnt += 1
            num //= divide
            divide = 2
        else:
            divide += 1

    if num > 1:
        prime_cnt += 1
        
    return prime_cnt

result = 0
for i in range(a, b+1):
    factor = factorization(i)
    if prime[factor] == 0:
        result += 1

print(result)