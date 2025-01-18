# 구간 합 구하기
import sys
input = sys.stdin.readline

def segment(left, right, node):
    if left == right:
        aggSum[node] = nums[right]
        return nums[right]

    mid = (left + right) // 2

    leftNode = segment(left, mid, node*2)
    rightNode = segment(mid+1, right, node*2+1)

    aggSum[node] = leftNode + rightNode

    return aggSum[node]

def query(left, right, nodeLeft, nodeRight, node):
    if left <= nodeLeft and  nodeRight <= right:
        return aggSum[node]

    if left > nodeRight or right < nodeLeft:
        return 0

    mid = (nodeLeft + nodeRight) // 2

    leftQuery = query(left, right, nodeLeft, mid, node*2)
    rightQuery = query(left, right, mid+1, nodeRight, node*2+1)

    return leftQuery + rightQuery

def update(idx, change, nodeLeft, nodeRight, node):
    if idx > nodeRight or idx < nodeLeft:
        return

    if nodeLeft == idx and nodeRight == idx:
        aggSum[node] += change
        return

    if nodeLeft <= idx and idx <= nodeRight:
        aggSum[node] += change
    
    mid = (nodeLeft + nodeRight) // 2

    update(idx, change, nodeLeft, mid, node*2)
    update(idx, change, mid+1, nodeRight, node*2+1)

n, m, k = map(int,input().split())

aggSum = [0] * (4*n)
nums = []

for i in range(n):
    num = int(input())
    nums.append(num)

segment(0, n-1, 1)

for i in range(m+k):
    a, b, c = map(int,input().split())

    if a == 1:
        update(b-1, c - nums[b-1], 0, n-1, 1)
        nums[b-1] = c
    else:
        print(query(b-1, c-1, 0, n-1, 1))
    
