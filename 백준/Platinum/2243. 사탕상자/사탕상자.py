# 사탕상자
import sys
input = sys.stdin.readline

def query(left, right, rank, Node):

    segTree[Node] -= 1
    
    if left == right:
          return left
        
    mid = (left + right) // 2

    if segTree[Node*2+1] >= rank:
        return query(left, mid, rank, Node*2+1)
    else:
        return query(mid+1, right, rank-segTree[Node*2+1], Node*2+2)

def change(left, right, idx, amount, Node):

    # 바꾸고자하는 idx 범위를 벗어난 경우
    if idx < left or idx > right:
        return segTree[Node]

    if left == right:
        segTree[Node] += amount
        return segTree[Node]

    mid = (left + right) // 2

    leftChange = change(left, mid, idx, amount, Node*2+1)
    rightChange = change(mid+1, right, idx, amount, Node*2+2)
    # 세그먼트 트리 갱신
    segTree[Node] = leftChange + rightChange

    return segTree[Node]
    
n = int(input())
segTree = [0] * (1000001*4)

for i in range(n):
    cmd = list(map(int,input().split()))

    if cmd[0] == 2:
        change(0, 1000000, cmd[1], cmd[2], 0)
    else:
        rank = cmd[1]
        result = query(0, 1000000, rank, 0)
        print(result)

