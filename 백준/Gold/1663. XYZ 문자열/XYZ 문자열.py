# XYZ 문자열
import sys
input = sys.stdin.readline

P = int(input()) # 문제번호
N = int(input()) 

X = [0] * 101
Y = [0] * 101
Z = [0] * 101
XYZ = [0] * 101

X[1] = 1
XYZ[1] = 1
word = ["X", "YZ", "ZX"]

for i in range(2, N+1):
    X[i] = Z[i-1]
    Y[i] = X[i-1]
    Z[i] = X[i-1] + Y[i-1]
    XYZ[i] = X[i] + Y[i] + Z[i]

if P == 1: # P가 1일경우 전체 문자열 갯수 출력
    print(XYZ[N])
elif P == 2:
    idx = int(input())
    cur = N
    while cur >= 4:
        front = XYZ[cur-3]
        tail = XYZ[cur-2]

        if front < idx:
            idx = idx - front
            cur = cur-2
        else:
            cur = cur-3

    print(word[cur-1][idx-1])
    
else: # P가 3일 경우 특정 문자의 갯수만 출력
    char = input().rstrip()

    if char == "X":
        print(X[N])
    elif char == "Y":
        print(Y[N])
    else:
        print(Z[N])
