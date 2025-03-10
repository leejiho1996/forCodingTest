# 수열과 쿼리 16
import sys
input = sys.stdin.readline

# 세그먼트 트리 구성
def makeTree(left, right, idx):
    if left == right:
        segTree[idx] = left
        return segTree[idx]
    
    mid = (left + right) // 2

    leftNode = makeTree(left, mid, idx*2+1)
    rightNode = makeTree(mid+1, right, idx*2+2)

    # left와 right 값 중 작은것으로 값 저장
    # 만약 같다면 left가 무조건 작으니 left 리턴
    if seq[leftNode] > seq[rightNode]:
        segTree[idx] = rightNode
    else:
        segTree[idx] = leftNode
        
    return segTree[idx]

def query(left, right, leftNode, rightNode, idx):
    # 범위를 벗어나면 최대값이 저장된 인덱스를 리턴
    if rightNode < left or right < leftNode: 
        return N
    # 찾고자하는 범위에 속하면 값을 리턴
    if left <= leftNode and rightNode <= right:
        return segTree[idx]

    mid = (leftNode + rightNode) // 2

    leftQuery = query(left, right, leftNode, mid, idx*2+1)
    rightQuery = query(left, right, mid+1, rightNode, idx*2+2)

    # left와 right 쿼리 값중 작은것으로 리턴
    # 만약 같다면 left가 무조건 작으니 left 리턴
    if seq[leftQuery] > seq[rightQuery]:
        return rightQuery
    else:
        return leftQuery

def changeNode(changeIdx, leftNode, rightNode, idx):
    # 범위를 벗어난 경우 바로 값을 리턴
    if changeIdx < leftNode or rightNode < changeIdx:
        return segTree[idx]

    # 바꾸고자하는 인덱스에 도달했을 때 값을 바꾼다
    if leftNode == rightNode:
        segTree[idx] = changeIdx
        return segTree[idx]

    mid = (leftNode + rightNode) // 2

    leftQuery = changeNode(changeIdx, leftNode, mid, idx*2+1)
    rightQuery = changeNode(changeIdx, mid+1, rightNode, idx*2+2)

    # left와 right 쿼리 값중 작은것으로 리턴
    # 만약 같다면 left가 무조건 작으니 left 리턴
    if seq[leftQuery] > seq[rightQuery]:
        segTree[idx] = rightQuery   
    else:
        segTree[idx] = leftQuery
        
    return segTree[idx]
    
N = int(input())
seq = list(map(int,input().split())) + [0]
# 마지막에 가짜 값을 만들어 최대값으로 설정
seq[-1] = 1_000_000_001 
M = int(input())
segTree = [0] * (N * 4 - 4)
makeTree(0, len(seq)-2, 0) # 세그먼트 트리를 만든다

for i in range(M):
    cmd, a, b = map(int,input().split())

    if cmd == 1:
        seq[a-1] = b
        changeNode(a-1, 0, N-1, 0)
    else:
        num = query(a-1, b-1, 0, N-1, 0)
        print(num+1)         
