# XOR 초간단
import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    S, F = map(int,input().split())

    S -= 1
    
    resultF = 0

    for j in range(F- (F % 4), F+1):
        resultF ^= j

    resultS = 0
    
    for j in range(S - (S % 4), S+1):
        resultS ^= j

    print(resultS ^ resultF)
