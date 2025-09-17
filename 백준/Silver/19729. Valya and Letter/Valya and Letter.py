# Valya and Letter 
import sys
input = sys.stdin.readline
from decimal import Decimal

N, M, H, W = map(int,input().split())
result = 130

N = Decimal(N)
M = Decimal(M)

for i in range(61):
    n = N / 2**i
    for j in range(61):
        m = M / 2**j
        
        if (n <= H and m <= W) or (m <= H and n <= W):
            result = min(result, i+j)

print(result)
    
