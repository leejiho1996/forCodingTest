# 특이한 수열
import sys
input = sys.stdin.readline

N, K = map(int,input().split())
result = [i for i in range(1, N+1)]
K = N - K

if K == 0:
    print("Impossible")
    exit()

if K == 1:
    print(*result)
    exit()

if K % 2 == 0:
    idx = 0
else:
    idx = 1

cnt = 0

while cnt < K // 2:
    result[idx], result[idx+1] = result[idx+1], result[idx]

    idx += 2
    cnt += 1

print(*result)

