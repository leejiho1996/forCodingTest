# 웜홀
import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n, m, w = map(int,input().split())
    upper = [0] * (n+1)
    edges = []
    check = False
    
    for j in range(m):
        s, e, t = map(int,input().split())
        edges.append((s,e,t))
        edges.append((e,s,t))
        
    for j in range(w):
        s, e, t = map(int,input().split())
        edges.append((s,e,-t))
        
    for j in range(n):
        for start, to, time in edges:
            if upper[start] + time < upper[to]:
                upper[to] = upper[start] + time

    for start, to, time in edges:
        if upper[start] + time < upper[to]:
                check = True
                break
    
    if check:
        print("YES")
    else:
        print("NO")
