# 소트
import sys
sys.stdin.readline

n = int(input())
elements = list(map(int,input().split()))
s = int(input())

def swap(idx, target):
    for i in range(idx, target, -1):
        tmp = elements[i]
        elements[i] = elements[i-1]
        elements[i-1] = tmp
        
for i in range(n):
    cur = elements[i]
    max_num = 0
    max_idx = -1
    max_move = 0
    for j in range(i+1, n):
        ch_num = elements[j]
        idx = j
        move = idx - i

        if ch_num <= cur or move > s:
            continue
        
        if ch_num > max_num:
            max_num = ch_num
            max_idx = idx
            max_move = move

    if max_idx != -1:
        s -= max_move
        swap(max_idx, i)
        
print(*elements)
