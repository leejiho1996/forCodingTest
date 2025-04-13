# 본대 산책2
import sys
input = sys.stdin.readline

def cal(m1, m2):
    
    nMatrix = [[0] * 8 for _ in range(8)]

    for i in range(8):
        for j in range(8):
            total = 0
            for k in range(8):
                total += (m1[i][k] * m2[k][j]) % MOD
                total %= MOD
                
            nMatrix[i][j] = total

    return nMatrix
            
def divide(n):

    if n == 1:
        return matrix
    
    result = divide(n//2)
    
    if n % 2 == 1:
        return cal(cal(result, result), matrix)
    else:
        return cal(result, result)

D = int(input())
MOD = 1_000_000_007
matrix = [[0, 1, 1, 0, 0, 0, 0, 0],
          [1, 0, 1, 1, 0, 0, 0, 0],
          [1, 1, 0, 1, 0 ,1, 0, 0],
          [0, 1, 1, 0, 1, 1, 0, 0],
          [0, 0, 0, 1, 0, 1, 1, 0],
          [0, 0, 1, 1, 1, 0, 0, 1],
          [0, 0, 0, 0, 1, 0, 0, 1],
          [0, 0, 0, 0, 0, 1, 1, 0]]

result = divide(D)
print(result[0][0])
