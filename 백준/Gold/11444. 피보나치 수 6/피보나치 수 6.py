# 피보나치 수 6

import sys
input = sys.stdin.readline

n = int(input())
mod = 1_000_000_007

matrix = [[1,1],
          [1,0]]

def product(matrix1, matrix2):
    
    result = [[0]*2 for _ in range(2)]

    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += (matrix1[i][k] * matrix2[k][j]) % mod
    return result

def divide(b):
    
    if b == 1:
        return matrix
    
    result = divide(b//2)

    if b % 2 == 1:
        return product(product(result, result), matrix) 
    else:
        return product(result, result)

if n == 0:
    print(0)
elif n == 1 or n == 2:
    print(1)
else:
    result = divide(n-1)
    print(result[0][0] % mod)