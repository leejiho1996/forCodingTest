# pqr
import sys
input = sys.stdin.readline

def gcd(a, b):
    if b > a:
        a, b = b, a

    while b:
        a, b = b, a % b
        
    return a

N, K = map(int,input().split())
nums = list(map(int,input().split()))
result = 0

sub = [0] * 1000001

for i in range(N):
    divide = 1
    cur = nums[i]
    
    while divide <= int(cur**0.5):
        if cur % divide == 0:
            sub[divide] += 1
            divided = cur // divide

            if divided != divide and divided <= 1000000:
                sub[cur//divide] += 1

        divide += 1

for i in range(N):
    n1 = nums[i]
    for j in range(i+1, N):
        n2 = nums[j]
        y = K // gcd(n1*n2, K)

        result += sub[y]
        
        if n1 % y == 0:
            result -= 1

        if n2 % y == 0:
            result -= 1
            
print(result // 3)
