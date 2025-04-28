# 월요일-토요일
import sys
input = sys.stdin.readline

prime = [0] * (300001)
prime[1] = 1

for i in range(2, 300001):
    if prime[i] == 1:
        continue
    
    if i % 7 == 1 or i % 7 == 6:
        for j in range(i+i, 300001, i):
            prime[j] = 1
    else:
        prime[i] = 1

while True:
    N = int(input())

    if N == 1:
        break

    pf = set()
    
    for i in range(1, int(N**0.5)+1):
        if N % i == 0:
            if prime[i] == 0:
                pf.add(i)

            if prime[N//i] == 0:
                pf.add(N//i)

    pf = list(pf)
    pf.sort()
    
    print(str(N) + ":", *pf )

    
