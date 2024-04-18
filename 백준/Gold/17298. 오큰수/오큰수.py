# 오큰수
import sys
input = sys.stdin.readline

a = int(input())
arr = list(map(int,input().split()))
result = [-1]*a
stack = []

for i in range(a):
    if i == 0:
        stack.append((arr[i], i))
        continue
    
    while stack and stack[-1][0] < arr[i]:
        num, idx = stack.pop()
        result[idx] = arr[i]
        
    stack.append((arr[i], i))
    
print(*result)