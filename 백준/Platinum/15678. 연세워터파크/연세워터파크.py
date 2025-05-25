# 연세워터파크
import sys
input = sys.stdin.readline

def find(left, right, leftNode, rightNode, node):
    if left > rightNode or right < leftNode:
        return -float('inf')

    if left >= leftNode and rightNode >= right:
        return segTree[node]

    mid = (left + right) // 2

    lf = find(left, mid, leftNode, rightNode, node*2+1)
    rf = find(mid+1, right, leftNode, rightNode, node*2+2)

    return max(lf, rf)

def update(left, right, idx, value, node):
    if left > idx or right < idx:
        return segTree[node]
    
    if left == right:
        segTree[node] = value
        return segTree[node]

    mid = (left + right) // 2

    lu = update(left, mid, idx, value, node*2+1)
    ru = update(mid+1, right, idx, value, node*2+2)

    segTree[node] = max(lu, ru)

    return segTree[node]
        
N, D = map(int,input().split())
bridge = list(map(int,input().split()))
dp = [-float('inf')] * N
segTree = [-float('inf')] * (N*4)
result = -float('inf')

for i in range(N-1, -1, -1):
    dp[i] = bridge[i]

    dp[i] = max(dp[i], dp[i] + find(0, N-1, i+1, min(N-1, i+D), 0))
    update(0, N-1, i, dp[i], 0)

print(max(dp))
