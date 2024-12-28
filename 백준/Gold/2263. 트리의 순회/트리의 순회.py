# 트리의 순회
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())

inorder = list(map(int,input().split()))
postorder = list(map(int,input().split()))

inorder_dic = {}

for i in range(n):
    inorder_dic[inorder[i]] = i
    
def tree(in_start, po_start, po_end):
    if po_start > po_end or in_start > n-1:
        return
    
    root = postorder[po_end]
    root_idx = inorder_dic[root] # inorder에서 루트 인덱스
    print(root, end = " ")
    
    left_count = root_idx - in_start
    right_count = (n-1) - root_idx
    
    tree(in_start, po_start, po_start+left_count-1) # 왼쪽
    tree(root_idx+1, po_start+left_count, po_end-1) # 오른쪽
    
tree(0, 0, n-1)         
