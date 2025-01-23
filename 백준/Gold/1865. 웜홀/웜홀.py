# 웜홀
import sys
input = sys.stdin.readline

def floyd():
    for k in range(1, n+1):
        for start in range(1, n+1):
            for to in range(1, n+1):
                if graph[start][k] + graph[k][to] < graph[start][to]:
                    graph[start][to] = graph[start][k] + graph[k][to]

                if start == to and graph[start][to] < 0:
                    return True
    return False

t = int(input())

for i in range(t):
    n, m, w = map(int,input().split())
    graph = [[10001] * (n+1) for _ in range(n+1)]
    wormhole = []
    check = False
    
    for j in range(m):
        s, e, t = map(int,input().split())
        graph[s][e] = graph[e][s] = min(graph[s][e], t)
        
    for j in range(w):
        s, e, t = map(int,input().split())
        graph[s][e] = min(graph[s][e], -t)

   
    if floyd():
        print("YES")
    else:
        print("NO")
