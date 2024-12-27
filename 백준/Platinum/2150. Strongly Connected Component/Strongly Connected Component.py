# SCC (타잔)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100001)

def tarjanSCC(n):
    global sccCnt
    global nodeCnt
    
    discoverd[n] = nodeCnt
    ret = nodeCnt
    nodeCnt += 1
    stack.append(n)
    
    for i in graph[n]:
        if not discoverd[i]:
            ret = min(ret, tarjanSCC(i))
        elif not group[i]:
            ret = min(ret, discoverd[i])

    if ret == discoverd[n]:
        scc = []
        while stack:
            cur = stack.pop()
            scc.append(cur)
            group[cur] = sccCnt
            
            if cur == n:
                scc.sort()
                scc.append(-1)
                result.append(scc)
                sccCnt += 1
                break
            
    return ret
    
v, e = map(int,input().split())
graph = [[] for _ in range(v+1)]
stack = []
result = []
discoverd = [0] * (v+1)
group = [0] * (v+1)
nodeCnt = 1
sccCnt = 1
for i in range(e):
    s, t = map(int,input().split())
    graph[s].append(t)

for i in range(1, v+1):
    if not discoverd[i]:
        tarjanSCC(i)

result.sort()
print(len(result))
for i in result:
    print(*i)
