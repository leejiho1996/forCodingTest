# 공항
import sys
input = sys.stdin.readline

def find(n):
    if gate[n] != n:
        gate[n] = find(gate[n])

    return gate[n]

G = int(input())
P = int(input())
cnt = 0

gate = [i for i in range(G+1)]

for i in range(P):
    num = int(input())
    toGo = find(num)

    if toGo <= 0:
        break
    else:
        cnt += 1
        gate[toGo] = find(toGo-1)

print(cnt)
