# 구름다리
import sys
input = sys.stdin.readline

N = int(input())
links = [[0] * (N+1) for _ in range(N+1)]
result = []

for i in range(N-1):
    n1, n2 = map(int,input().split())
    links[n1][n2] = 1
    links[n2][n1] = 1

cnt = 0

for i in range(1, N+1):
    if cnt == N-1:
        break
    
    for j in range(i+1, N+1):
        if links[i][j] == 0:
            links[i][j] = 1
            result.append((i, j))
            
            cnt += 1

            if cnt == N-1:
                break
            
print(len(result))
    
if N >= 5:
    print(2)
else:
    print(1)

for i in result:
    print(*i)
