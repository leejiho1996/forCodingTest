# Psuedo-Random Numbers
import sys
input = sys.stdin.readline

cases = 1

while True:
    Z, I, M, L = map(int,input().split())

    if Z == 0 and I == 0 and M == 0 and L == 0:
        break

    visited = [0] * 10000
    cnt = 0
    
    while True:
        L = (L * Z + I) % M

        if visited[L]:
            print(f'Case {cases}: {cnt}')
            break

        visited[L] = 1
        cnt += 1

    cases += 1
    