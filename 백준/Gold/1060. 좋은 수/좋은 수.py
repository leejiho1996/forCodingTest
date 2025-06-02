# 좋은 수
import sys
input = sys.stdin.readline

def count(s, e):
    
    total = 0
    idx = 0
    mid = (s + e) // 2
    
    for i in range(s, mid+1):
        cnt = (e-i) + ((e-i+1) * (i-s))
        result.append((cnt, i))

        if (i != e-idx):
            result.append((cnt, e-idx))
            total += 1
            
        idx += 1
        total += 1
        
        if total >= N:
            break

L = int(input())
S = list(map(int,input().split()))
N = int(input())

S.sort()

result = []
for i in S:
    result.append((0, i))

start = 1

for i in range(L):
    end = S[i] - 1
    count(start, end)
    start = S[i]+1

result.sort()

if len(result) < N:
    for i in range(N - len(result)):
        result.append((-1, S[-1] + 1 + i))

for i in range(N):
    print(result[i][1], end = " ")
