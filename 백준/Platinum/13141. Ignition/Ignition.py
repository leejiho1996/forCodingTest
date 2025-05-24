# ignition
import sys
input = sys.stdin.readline

def floyd():
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if distances[i][j] > distances[i][k] + distances[k][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]

N, M = map(int,input().split())

edges = []
distances = [[float('inf')] * (N+1) for _ in range(N+1)]
result = float('inf')

for i in range(1, N+1):
    distances[i][i] = 0
    
for i in range(M):
    s, e, l = map(int,input().split())

    distances[s][e] = min(distances[s][e], l)
    distances[e][s] = min(distances[e][s], l)
    edges.append((s, e, l))

floyd()

for i in range(1, N+1):
    tmp = 0

    for s, e, l in edges:
        start = min(distances[i][s], distances[i][e])
        abss = abs(distances[i][s] - distances[i][e])

        start += abss
        start += (l - abss) / 2
        tmp = max(tmp, start)

    result = min(result, tmp)

print(result)
