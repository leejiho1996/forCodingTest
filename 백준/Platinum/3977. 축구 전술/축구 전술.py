# 축구전술
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000001)

def tarjan(n):
    global nodeCnt
    global sccCnt

    stack.append(n)
    discoverd[n] = nodeCnt
    ret = nodeCnt
    nodeCnt += 1

    for child in graph[n]:
        if discoverd[child] == -1:
            ret = min(ret, tarjan(child))
        elif sccGroup[child] == -1:
            ret = min(ret, discoverd[child])

    if ret == discoverd[n]:
        scc = []
        while stack:
            cur = stack.pop()
            scc.append(cur)
            sccGroup[cur] = sccCnt
            
            if cur == n:
                result.append(scc)
                sccCnt += 1
                break
    return ret

t = int(input())
for i in range(t):
    if i != 0:
        print(input().rstrip())

    n, m = map(int,input().split())
    graph = [[] for _ in range(n)]
    discoverd = [-1] * n 
    sccGroup = [-1] * n
    result = [] # scc 집합을 담을 리스트
    stack = []
    nodeCnt = 1
    sccCnt = 1

    for j in range(m):
        s, t = map(int,input().split())
        graph[s].append(t)

    for j in range(n):
        if discoverd[j] == -1:  
            tarjan(j)

    front = [0] * sccCnt
    
    for j in range(n):
        for k in graph[j]:
            if sccGroup[j] != sccGroup[k]:
                front[sccGroup[k]] += 1

    if front.count(0) > 2:
        print("Confused")
    else:
        result[-1].sort()
        for j in result[-1]:
            print(j)
        
        
