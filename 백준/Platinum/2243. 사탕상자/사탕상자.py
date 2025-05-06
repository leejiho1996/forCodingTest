# 사탕상자
import sys
input = sys.stdin.readline

def query(left, right, rank, Node):
    # 해당 노드의 값 -1
    segTree[Node] -= 1
    
    if left == right:
          return left
        
    mid = (left + right) // 2

    # 왼쪽 자식노드가 찾는 순위보다 같거나 크다면 해당 부분을 탐색
    if segTree[Node*2+1] >= rank:
        return query(left, mid, rank, Node*2+1)
    # 왼쪽 자식 노드가 찾는 순위보다 작다면 rank를 해당 값만 큼 빼주고 오른쪽 탐색
    else: 
        return query(mid+1, right, rank-segTree[Node*2+1], Node*2+2)

def change(left, right, idx, amount, Node):

    segTree[Node] += amount

    if left == right:
        return segTree[Node]

    mid = (left + right) // 2

    if mid >= idx:
        return change(left, mid, idx, amount, Node*2+1)
    else:
        return change(mid+1, right, idx, amount, Node*2+2)
        
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

