# 고라니 컨트롤
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
pos = []

for i in range(N-1):
    num = int(input())
    pos.append((i, 0, num))

nums = list(map(int,input().split()))

for i in range(M):
    pos.append((N-1, i, nums[i]))

for i in range(N):
    for j in range(M):
        check = True
        
        for r, c, num in pos:

            if abs(r - i) + abs(c - j) != num:
                check = False
                break

        if check:
            print(i+1, j+1)
    
