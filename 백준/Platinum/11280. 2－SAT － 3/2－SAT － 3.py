# 2-SAT-3
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000001)

def tarjan(n):
    global nodeCnt
    global sccCnt

    stack.append(n)
    discovered[n] = nodeCnt
    ret = nodeCnt
    nodeCnt += 1

    for child in graph[n]:
        if not discovered[child]:
            ret = min(ret, tarjan(child))
        elif not sccGroup[child]:
            ret = min(ret, discovered[child])

    if ret == discovered[n]:
        while stack:
            cur = stack.pop()
            sccGroup[cur] = sccCnt

            if cur == n:
                sccCnt += 1
                break

    return ret

def solveNot(num):
    if num > n:
        return num - n
    else:
        return num + n

n, m = map(int,input().split())
graph = [[] for _ in range(2*n+1)]
discovered = [0] * (2*n+1)
sccGroup = [0] * (2*n+1)
stack = []
nodeCnt = 1
sccCnt = 1

for i in range(m):
    b1, b2 = map(int,input().split())
    if b1 < 0:
        b1 = -b1
    else:
        b1 = b1 + n

    if b2 < 0:
        b2 = -b2
    else:
        b2 = b2 + n
        
    graph[solveNot(b1)].append(b2)
    graph[solveNot(b2)].append(b1)

for i in range(1, 2*n+1):
    if not discovered[i]:
        tarjan(i)

for i in range(1, 2*n+1):
    if sccGroup[i] == sccGroup[solveNot(i)]:
        print(0)
        exit()
print(1)
