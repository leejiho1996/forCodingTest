# 이전 수열은 어떤 수열일까
import sys
input = sys.stdin.readline

N = int(input())
origin = []
idx = [-1] * (N+1)
result = [0] * N

for i in range(N):
    num = int(input())
    origin.append(num)
    idx[num] = i

for i in range(N):
    cur = origin[i]

    if idx[cur] == -1:
        continue
    
    m1 = idx[cur-1]

    if m1 == 0 or m1 < idx[cur]:
        result[i] = cur
    else:
        result[i] = cur-1
        result[m1] = cur

        idx[cur-1] = -1
        idx[cur] = -1

for i in result:
    print(i)
    