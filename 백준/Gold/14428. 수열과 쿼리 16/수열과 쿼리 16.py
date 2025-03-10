# 수열과 쿼리 16
import sys
input = sys.stdin.readline

def makeTree(left, right, idx):
    if left == right:
        segTree[idx] = left
        return segTree[idx]
    
    mid = (left + right) // 2

    leftNode = makeTree(left, mid, idx*2+1)
    rightNode = makeTree(mid+1, right, idx*2+2)

    if seq[leftNode] > seq[rightNode]:
        segTree[idx] = rightNode
    else:
        segTree[idx] = leftNode
        
    return segTree[idx]

def query(left, right, leftNode, rightNode, idx):
    if rightNode < left or right < leftNode:
        return N

    if left <= leftNode and rightNode <= right:
        return segTree[idx]

    mid = (leftNode + rightNode) // 2

    leftQuery = query(left, right, leftNode, mid, idx*2+1)
    rightQuery = query(left, right, mid+1, rightNode, idx*2+2)

    if seq[leftQuery] > seq[rightQuery]:
        return rightQuery
    else:
        return leftQuery

def changeNode(changeIdx, leftNode, rightNode, idx):
    if changeIdx < leftNode or rightNode < changeIdx:
        return segTree[idx]

    if leftNode == rightNode:
        segTree[idx] = changeIdx
        return segTree[idx]

    mid = (leftNode + rightNode) // 2
    
    leftQuery = changeNode(changeIdx, leftNode, mid, idx*2+1)
    rightQuery = changeNode(changeIdx, mid+1, rightNode, idx*2+2)

    if seq[leftQuery] > seq[rightQuery]:
        segTree[idx] = rightQuery
        return segTree[idx]
    else:
        segTree[idx] = leftQuery
        return segTree[idx]
    
N = int(input())
seq = list(map(int,input().split())) + [0]
seq[-1] = 1_000_000_001
M = int(input())
segTree = [0] * (len(seq) * 4 + 1)
makeTree(0, len(seq)-2, 0)

for i in range(M):
    cmd, a, b = map(int,input().split())

    if cmd == 1:
        seq[a-1] = b
        changeNode(a-1, 0, N-1, 0)
    else:
        num = query(a-1, b-1, 0, N-1, 0)
        print(num+1)         
