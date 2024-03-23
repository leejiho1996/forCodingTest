# 행렬 제곱

import sys
input = sys.stdin.readline

n, b = map(int,input().split())

matrix = [list(map(int,input().split())) for _ in range(n)]

def reshape(matrix):
    matrix_reshape = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrix_reshape[i].append(matrix[j][i])
    return matrix_reshape

def product(matrix1, matrix2):

    reshape_matrix = reshape(matrix2)
    
    result = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            cnt = 0
            for k in range(n):
                cnt += matrix1[i][k] * reshape_matrix[j][k]
            result[i].append(cnt % 1000)

    return result

def divide(b):
    if b == 1:
        return matrix

    result = divide(b//2)

    if b % 2 == 1:
        return product(product(result, result), matrix) 
    else:
        return product(result, result)

for i in divide(b):
    for j in i:
        print(j % 1000, end = ' ')
    print()
