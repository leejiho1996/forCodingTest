# 타일 채우기2
import sys
input = sys.stdin.readline

MOD = 1_000_000_007

# 분할정복 함수
def divide(n):
    if n == 1:
        return [[4, -1],
                [1, 0]]

    sqrt = divide(n//2)

    if n % 2 == 1:
        return multiplyMatrix(multiplyMatrix(sqrt, sqrt), [[4, -1], [1, 0]])
    else:
        return multiplyMatrix(sqrt, sqrt)
        

# 행렬곱 함수
def multiplyMatrix(m1, m2):
    result = [[0,0],
              [0,0]]

    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += m1[i][k] * m2[k][j]
            result[i][j] %= MOD

    return result


n = int(input())

if n % 2:
    print(0)
else:
    base = [[3, 0],
            [1, 0]]
    
    divideCnt = n // 2
    result = divide(divideCnt)
    print(multiplyMatrix(result, base)[1][0])
    
