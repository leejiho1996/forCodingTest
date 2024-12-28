# 트리의 순회
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

n = int(input())

inOrder = list(map(int,input().split()))
postOrder = list(map(int,input().split()))
inOrderIdx = [-1] * (n+1)

for i in range(n):
    node = inOrder[i]
    inOrderIdx[node] = i

def preOrder(inStart, postStart, postEnd):
    if inStart >= n or postStart > postEnd:
        return

    root = postOrder[postEnd]
    rootIdx = inOrderIdx[root]
    print(root)
    
    rightPostStart = postStart + rootIdx - inStart
    rightPostEnd = postEnd - 1
    

    preOrder(inStart, postStart, rightPostStart-1)
    preOrder(rootIdx+1, rightPostStart, rightPostEnd)

preOrder(0, 0, n-1)
