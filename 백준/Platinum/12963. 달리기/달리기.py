# 달리기
import sys
input = sys.stdin.readline

def find(n):
    if parent[n] != n:
        parent[n] = find(parent[n])

    return parent[n]

N, M = map(int,input().split())
roads = []
parent = [i for i in range(N)]
result = 0
MOD = 1_000_000_007

multiply = 1
for i in range(M):
    a, b = map(int,input().split())
    roads.append((a, b, multiply))
    multiply *= 3

for i in range(M-1, -1, -1):
    a, b, cost = roads[i]

    pa, pb = find(a), find(b)
    ps, pe = find(0), find(N-1)

    if ((pa == ps and pb == pe) or (pa == pe and pb == ps)):
        result += cost
        result %= MOD
    else:
        parent[pa] = pb

print(result)