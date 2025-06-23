# 출석체크
import sys
input = sys.stdin.readline

N, K, Q, M = map(int,input().split())
sleeps = set(map(int,input().split()))
codes = list(map(int,input().split()))

takes = [1] * (N+3)

for i in codes:
    if i in sleeps:
        continue
    
    for j in range(i, N+3, i):
        if j in sleeps:
            continue
        
        takes[j] = 0

aggSum = [0] * (N+3)

for i in range(3, N+3):
    aggSum[i] = aggSum[i-1] + takes[i]

for i in range(M):
    S, E = map(int,input().split())
    print(aggSum[E] - aggSum[S-1])
