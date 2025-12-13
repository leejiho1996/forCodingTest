# K-세준수
import sys
input = sys.stdin.readline

N = int(input())
K = int(input())

sosu = [0] * (N+1)
result = [0] * (N+1)

for i in range(2, N+1):
    if sosu[i] == 0:
        cur = 2*i

        if i > K:
            result[i] = 1
            
        while cur <= N:
            if i > K:
                result[cur] = 1
                
            sosu[cur] = 1
            cur += i

print(N-sum(result))
