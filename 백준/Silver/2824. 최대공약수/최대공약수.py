# 최대공약수
import sys
input = sys.stdin.readline

def gcd(a, b):
    if a < b:
        a, b = b, a

    while b > 0:
        a, b = b, a % b

    return a

N = int(input())
n_nums = list(map(int,input().split()))

M = int(input())
m_nums = list(map(int,input().split()))

result = 1

for i in range(N):
    for j in range(M):
        gcd_nums = gcd(n_nums[i], m_nums[j])
        result *= gcd_nums
        n_nums[i] //= gcd_nums
        m_nums[j] //= gcd_nums

if len(str(result)) > 9:
    print(str(result)[-9:])
else:
    print(result)
