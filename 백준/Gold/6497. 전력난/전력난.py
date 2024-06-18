# 전력난
import sys
input = sys.stdin.readline

def find(n):
    if parent[n] != n:
        parent[n] = find(parent[n])
    return parent[n]


while True:
    m, n = map(int,input().split())
    if m == 0 and n == 0:
        break
    
    edge = []
    parent = [i for i in range(m)]
    total_cost = 0
    
    for i in range(n):
        start, to, cost = map(int,input().split())
        edge.append((cost, start, to))
        total_cost += cost
        
    edge.sort()
    total = 0
    
    for cost, start, to in edge:
        s_p = find(start)
        t_p = find(to)

        if s_p != t_p:
            if s_p > t_p:
                parent[s_p] = t_p
            else:
                parent[t_p] = s_p

            total += cost
    
    print(total_cost - total)
