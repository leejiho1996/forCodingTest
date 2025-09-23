# 문자열
import sys
input = sys.stdin.readline

minn = 100
A, B = input().rstrip().split()

for i in range(len(B)):
    tmp = 0
    for j in range(len(A)):
        if i + len(A) - 1 >= len(B):
            tmp = 100
            break
        
        if A[j] != B[i+j]:
            tmp += 1

    minn = min(minn, tmp)

print(minn)
