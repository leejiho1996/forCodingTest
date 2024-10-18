# 탑 보기
import sys
input = sys.stdin.readline

n = int(input())
towers = list(map(int,input().split()))
left = []
right = []
stack = []
cnt = 0

for i in range(n):
    tower = towers[i]
    while stack and stack[-1][0] <= tower:
        stack.pop()

    if stack:
        idx = stack[-1][1]
        left.append((len(stack), idx+1, i - idx))
    else:
        left.append((len(stack), 100001, 100001))
        
    stack.append((tower, i)) 

stack = []          
for i in range(n-1, -1, -1):
    tower = towers[i]
    while stack and stack[-1][0] <= tower:
        stack.pop()

    if stack:
        idx = stack[-1][1]
        right.append((len(stack), idx+1, idx - i))
    else:
        right.append((len(stack), 100001, 100001))
        
    stack.append((tower, i))

right = right[::-1]

for i in range(n):
    summ = right[i][0] + left[i][0]
    l_dis = left[i][2]
    r_dis = right[i][2]
    if summ == 0:
        print(0)
    else:
        if l_dis <= r_dis:
            distance = left[i][1]
        else:
            distance = right[i][1]
        print(summ, distance)
