# 플로이드에 오타가?
import sys
input = sys.stdin.readline

D = [[0] * 100 for _ in range(100)]

for i in range(99):
    for j in range(100):
        if i == j:
            continue

        if j == 9999:
            D[i][j] = 1
            continue
        
        D[i][j] = 2

for i in range(99):
    D[i][j] = 1

print(100)

for i in range(100):
    print(*D[i])
