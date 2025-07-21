# 사람의 수
import sys
input = sys.stdin.readline

N = int(input())
scores = []

for i in range(N):
    integer, floating = input().rstrip().split(".")
    scores.append(int(integer) * 1000 + int(floating))

for i in range(1, 1001):
    cnt = 0

    for j in range(N):
        total = scores[j] * i

        if total % 1000 != 0:
            total = (total // 1000+1) * 1000
        
        if total // i == scores[j]:
            cnt += 1

    if cnt == N:
        break
        
print(i)
            
