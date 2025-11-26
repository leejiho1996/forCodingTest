# 캔 주기
import sys
input = sys.stdin.readline

def brute(cur, total):
    global result
    
    if cur == K:
        result = max(result, total)
        return

    for i in range(N):
        if cans[i] == 0:
            continue

        cans[i] -= 1
        
        for j in range(N):
            if cans[j] == 0:
                continue
            
            cans[j] -= 1
            brute(cur+1, total + rang[cur][i] + merry[cur][j])
            cans[j] += 1

        cans[i] += 1
            
N, K = map(int,input().split())
cans = list(map(int,input().split()))
result = 0

rang = []
merry = []

for i in range(K):
    rang.append(list(map(int,input().split())))

for i in range(K):
    merry.append(list(map(int,input().split())))

brute(0, 0)

print(result)
