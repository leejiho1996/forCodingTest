# 행렬
import sys
input = sys.stdin.readline

def change(r, c):
    for i in range(r, r+3):
        for j in range(c, c+3):
            if A[i][j] == '0':
                A[i][j] = '1'
            else:
                A[i][j] = '0'

N, M = map(int,input().split())

A = []
B = []

for i in range(N):
    A.append(list(input().rstrip()))

for i in range(N):
    B.append(list(input().rstrip()))

cnt = 0

for i in range(N-2):
    for j in range(M-2):

        if A[i][j] != B[i][j]:
            cnt += 1
            change(i, j)

for i in range(N):
    for j in range(M):
        if A[i][j] != B[i][j]:
            print(-1)
            exit()

print(cnt)
    
