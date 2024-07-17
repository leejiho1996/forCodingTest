# 사이클 게임
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

def find(n):
    if n != parent[n]:
        parent[n] = find(parent[n])
    return parent[n]

parent = [i for i in range(n)]

for i in range(m):
    start, end = map(int,input().split())
    start_p = find(start)
    end_p = find(end)

    if start_p != end_p:
        if start_p > end_p:
            parent[start_p] = end_p
        else:
            parent[end_p] = start_p
    else:
        print(i+1)
        exit()

print(0)
