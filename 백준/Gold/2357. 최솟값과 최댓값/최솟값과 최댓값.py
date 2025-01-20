# 최솟값과 최대값
import sys
input = sys.stdin.readline

MIN = 0
MAX = 1_000_000_000

def segment(left, right, node):
    if left == right:
        minMax[node] = [nums[right], nums[right]]
        return minMax[node]

    mid = (left + right) // 2

    left = segment(left, mid, node*2)
    right = segment(mid+1, right, node*2+1)
    minMax[node] = [min(left[0], right[0]), max(left[1], right[1])]

    return minMax[node]

def query(left, right, leftNode, rightNode, node):
    if rightNode < left or leftNode > right:
        return [MAX, MIN]

    if left <= leftNode and rightNode <= right:
        return minMax[node]

    mid = (leftNode + rightNode) // 2
    
    leftQuery = query(left, right, leftNode, mid, node*2)
    rightQuery = query(left, right, mid+1, rightNode, node*2+1)

    return [min(leftQuery[0], rightQuery[0]),
            max(leftQuery[1], rightQuery[1])]
    
n, m = map(int,input().split())
nums = []
minMax = [[MAX, MIN]] * (4*n)

for i in range(n):
    nums.append(int(input()))

segment(0, n-1, 1)
for j in range(m):
    left, right = map(int,input().split())
    print(*query(left-1, right-1, 0, n-1, 1))
