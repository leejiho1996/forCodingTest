# 이진 검색 트리
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100001)

prev = 0

node = []

while True:
    try:
        n = int(input())
        node.append(n)        
    except:
        break
    
def post(left, right):
    if left > right:
        return

    border = right + 1
    
    for i in range(left+1, right+1):
        if node[i] > node[left]:
            border = i
            # print("border", border)
            break

    post(left+1, border-1)
    post(border, right)
    print(node[left])
    
post(0, len(node)-1)
