# 올림픽
import sys
input = sys.stdin.readline

n, k = map(int,input().split())
medals = []
result = [0] * (n+1)

for i in range(n):
    medals.append(list(map(int,input().split())))

medals.sort(key = lambda x : (x[1], x[2], x[3]), reverse = True)

cnt = 1
for i in range(n):
    idx, g, s, b = medals[i]
    
    if result[idx] != 0:
        continue
    else:
        cur = cnt
        result[idx] = cnt

    for j in range(i+1, n):
        oidx, og, os, ob = medals[j]

        if g > og or s > os or b > ob:
            cnt += 1
            break
        else:
            result[oidx] = cur
            cnt += 1

print(result[k])
