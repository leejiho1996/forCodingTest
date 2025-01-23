# 웜홀
import sys
input = sys.stdin.readline

def bellmanford(n, upper, edges):
    for j in range(n-1):
        for start, to, time in edges:
            if upper[start] + time < upper[to]:
                upper[to] = upper[start] + time

    for start, to, time in edges:
        if upper[start] + time < upper[to]:
                return True

    return False
    
t = int(input())

for i in range(t):
    n, m, w = map(int,input().split())
    upper = [0] * (n+1)
    edges = []
    
    for j in range(m):
        s, e, t = map(int,input().split())
        edges.append((s,e,t))
        edges.append((e,s,t))
        
    for j in range(w):
        s, e, t = map(int,input().split())
        edges.append((s,e,-t))
        
    if bellmanford(n, upper, edges):
        print("YES")
    else:
        print("NO")
