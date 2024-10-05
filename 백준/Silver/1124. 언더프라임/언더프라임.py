# 언더프라임
import sys
input = sys.stdin.readline

a, b = map(int,input().split())

prime = [0] * (b+1)
prime_set = set()

for i in range(2, b+1):
    num = i
    if prime[num] == 0:
        prime_set.add(num)
        prime[num] = num
        cnt = 2
        while num*cnt < b+1:
            prime[num*cnt] = num
            cnt += 1

result = 0
for i in range(a, b+1):
    num = i
    cnt = 0
    while num > 1:
        cnt += 1
        num //= prime[num]

    if cnt in prime_set:
        result += 1
        
print(result)