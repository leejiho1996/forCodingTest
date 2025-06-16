# 역습
import sys
input = sys.stdin.readline

C = int(input())

for i in range(C):
    N, L1, L2, S1, S2 = map(int,input().split())
    dp1 = [0] * N
    dp2 = [0] * N

    dp1[0] = L1
    dp2[0] = L2
    
    S1Pass = list(map(int,input().split()))
    S1Drib = list(map(int,input().split()))

    S2Pass = list(map(int,input().split()))
    S2Drib = list(map(int,input().split()))

    for j in range(1, N):
        dp1[j] = min(dp1[j-1] + S1Drib[j-1], dp2[j-1] + S2Pass[j-1])
        dp2[j] = min(dp2[j-1] + S2Drib[j-1], dp1[j-1] + S1Pass[j-1])

    print(min(dp1[N-1] + S1, dp2[N-1] + S2))
        
