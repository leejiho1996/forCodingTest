# 행성 터널
import sys
input = sys.stdin.readline

def find(n):
    if parent[n] != n:
        parent[n] = find(parent[n])

    return parent[n]

N = int(input())
parent = [i for i in range(N)]
total = 0

X = []; Y = []; Z = [] 

for i in range(N):
    x, y, z = map(int,input().split())
    X.append((x, i))
    Y.append((y, i))
    Z.append((z, i))

X.sort(); Y.sort(); Z.sort(); # X, Y, Z 좌표 정렬

edges = []

for i in range(N-1):
    distX = X[i+1][0] - X[i][0]
    distY = Y[i+1][0] - Y[i][0]
    distZ = Z[i+1][0] - Z[i][0]

    edges.append((distX, X[i+1][1], X[i][1]))
    edges.append((distY, Y[i+1][1], Y[i][1]))
    edges.append((distZ, Z[i+1][1], Z[i][1]))

edges.sort()

for dist, n1, n2 in edges:
    p1 = find(n1)
    p2 = find(n2)

    if p1 != p2:
        parent[p1] = p2
        total += dist

print(total)
