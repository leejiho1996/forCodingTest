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
        cur = scores[j]
        for k in range(i*10+1):
            if int(k / i * 1000) == cur:
                cnt += 1
                break

    if cnt == N:
        break

print(i)
            
