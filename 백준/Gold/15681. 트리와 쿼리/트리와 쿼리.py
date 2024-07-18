# 트리와 쿼리
import sys
input =sys.stdin.readline
sys.setrecursionlimit(1000001)

n, r, q = map(int,input().split())

edges = [[] for _ in range(n+1)]
child = [[] for _ in range(n+1)] 
countChild = [1] * (n+1)

for i in range(n-1):
    start, end = map(int,input().split())
    edges[start].append(end)
    edges[end].append(start)

def makeTrees(currentNode, parent):
    for node in edges[currentNode]:
        if node != parent:
            child[currentNode].append(node)
            countChild[currentNode] += makeTrees(node, currentNode)

    return countChild[currentNode]

makeTrees(r,-1)

for i in range(q):
    question = int(input())
    print(countChild[question])
