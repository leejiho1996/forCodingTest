# 집합의 표현
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000001)

n, m = map(int,input().split())

parent = [i for i in range(n+1)]

def find(n):
    if parent[n] != n:
        parent[n] = find(parent[n])
    return parent[n]

for i in range(m):
    command, a, b = map(int,input().split())
    p_a = find(a)
    p_b = find(b)

    if command == 0:
        if p_a > p_b:
            parent[p_a] = p_b
        else:
            parent[p_b] = p_a
    else:
        if p_a == p_b:
            print("YES")
        else:
            print("NO")
        
