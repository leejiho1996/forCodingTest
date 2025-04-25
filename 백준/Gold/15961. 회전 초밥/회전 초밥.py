# 회전 초밥
import sys
input = sys.stdin.readline

N, d, k, c = map(int,input().split())
sushi = []
types = [0] * (d+1)
cnt = 1

types[c] += 1

for i in range(N):
    sushi.append(int(input()))

for i in range(k):
    if types[sushi[i]] == 0:
        cnt += 1
        types[sushi[i]] = 1
    else:
        types[sushi[i]] += 1

result = cnt
for i in range(1, N):
    nex = sushi[(i + (k-1)) % N]
    prev = sushi[i-1]

    types[prev] -= 1
    if types[prev] == 0:
        cnt -= 1

    types[nex] += 1
    if types[nex] == 1:
        cnt += 1
        
    result = max(result, cnt)

print(result)   
