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

dic = {}

for i in range(N):
    y = gcd(nums[i], K)

    if y in dic:
        dic[y] += 1
    else:
        dic[y] = 1

pairs = list(dic.items())
length = len(pairs)

for i in range(length):
    ki, vi = pairs[i]
    for j in range(i, length):
        kj, vj = pairs[j]
        for k in range(j, length):
            kk, vk = pairs[k]

            if ki * kj * kk % K != 0:
                continue

            if i == j == k:
                result += vi * (vi-1) * (vi-2) // 6

            elif i == j:
                result += vi * (vi-1) * vk // 2

            elif j == k:
                result += vi * vj * (vk-1) // 2

            else:
                result += vi * vj * vk
                 
print(result)
