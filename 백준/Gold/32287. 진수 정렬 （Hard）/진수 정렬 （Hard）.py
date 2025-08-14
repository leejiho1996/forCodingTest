# 진수 정렬(Hard)
import sys
input = sys.stdin.readline

N, M = map(int,input().split())

S = input().rstrip()
nums = [0] * 10
factorial = [0] * (N+1)
factorial[0] = 1

for i in S:
   nums[int(i)] += 1

for i in range(1, N+1):
    factorial[i] = factorial[i-1] * i

prev = 0
bigger = 0

for i in range(M-1, 0, -1): 
    cur = nums[i]

    denom_fixed = 1           
    for t in range(i+1, M):   
        denom_fixed *= factorial[nums[t]]  

    for j in range(cur-1, -1, -1):
        fixed = factorial[N] // (denom_fixed * factorial[j])
        free = (N - bigger - j) 

        prev += fixed * i**(free) // factorial[free]

    bigger += cur

for i in range(N-1, -1, -1):  
    cur = int(S[i])

    for j in range(cur-1, -1, -1):
        if nums[j] == 0:
            continue
        base = factorial[i]

        nums[j] -= 1
        for k in range(M-1, -1, -1):
            base //= factorial[nums[k]]
        nums[j] += 1

        prev += base

    nums[cur] -= 1

print(prev) 
