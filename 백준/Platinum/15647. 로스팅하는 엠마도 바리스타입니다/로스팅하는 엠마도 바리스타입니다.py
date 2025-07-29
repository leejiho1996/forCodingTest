# 로스팅 하는 엠마도 바리스타 입니다
import sys
input = sys.stdin.readline
sys.setrecursionlimit(300002)

def calRoot(root, prev, cur, dist):

    total[root] += dist
    ret = 0
    
    for i, d in graph[cur]:
        if i == prev:
            continue

        ret += 1
        ret += calRoot(root, cur, i, dist+d)

    childs[cur] = ret
        
    return ret
    
def calDist(prev, cur, dist):

    shorter = childs[cur] * dist
    longer = (N - childs[cur] - 2) * dist

    total[cur] += total[prev] + longer - shorter

    for i, d in graph[cur]:
        if i == prev:
            continue

        calDist(cur, i, d)
        
N = int(input())
total = [0] * (N+1)
childs = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for i in range(N-1):
    n1, n2, dist = map(int,input().split())

    graph[n1].append((n2, dist))
    graph[n2].append((n1, dist))

calRoot(1, -1, 1, 0)
calDist(-1, 1, 0)

for i in range(1, N+1):
    print(total[i])
