# 구간 곱 구하기
import sys
input = sys.stdin.readline

MOD = 1_000_000_007

# 세그먼트 트리 생성 함수
def segment(left, right, node):
    global zeroIdx
    
    if left == right:
        aggSum[node] = nums[right]
        return nums[right]

    mid = (left + right) // 2

    leftNode = segment(left, mid, node*2)
    rightNode = segment(mid+1, right, node*2+1)

    aggSum[node] = leftNode * rightNode % MOD

    return aggSum[node]

# left-right 구간의 구간 곱을 구하는 함수
def query(left, right, nodeLeft, nodeRight, node):
    if left <= nodeLeft and  nodeRight <= right:
        return aggSum[node]

    if left > nodeRight or right < nodeLeft:
        return 1

    mid = (nodeLeft + nodeRight) // 2

    leftQuery = query(left, right, nodeLeft, mid, node*2)
    rightQuery = query(left, right, mid+1, nodeRight, node*2+1)

    return leftQuery * rightQuery % MOD

def update(idx, change, nodeLeft, nodeRight, node):
    if idx > nodeRight or idx < nodeLeft:
        return aggSum[node]

    if nodeLeft == idx and nodeRight == idx: # idx까지 왔다면 갱신 후 return
        aggSum[node] = change
        return aggSum[node]

    mid = (nodeLeft + nodeRight) // 2

    left = update(idx, change, nodeLeft, mid, node*2)
    right = update(idx, change, mid+1, nodeRight, node*2+1)
    aggSum[node] = left*right % MOD
    
    return aggSum[node]
    
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
        update(b-1, c, 0, n-1, 1)
        nums[b-1] = c
    else:
        print(query(b-1, c-1, 0, n-1, 1))
    
