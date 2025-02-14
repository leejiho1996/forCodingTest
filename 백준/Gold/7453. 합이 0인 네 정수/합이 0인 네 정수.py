# 합인 0인 네 정수
import sys
input = sys.stdin.readline

n = int(input())
A = [0] * n
B = [0] * n
C = [0] * n
D = [0] * n

square = n**2
AB = [] # A와 B를 더한 전체 값
CD = {} # C와 D를 더한 전체 값

for i in range(n):
    row = list(map(int,input().split()))
    A[i] = row[0]
    B[i] = row[1]
    C[i] = row[2]
    D[i] = row[3]

for i in range(n):
    a = A[i]
    c = C[i]
    for j in range(n):
        AB.append(a+B[j])
        if c+D[j] in CD:
            CD[c+D[j]] += 1
        else:
            CD[c+D[j]] = 1

result = 0

for i in range(square):
    cur = AB[i]
    start = 0
    end = square-1
    target = 0 - cur

    if target in CD:
        result+=CD[target]

print(result)
    
