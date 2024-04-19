# 오등큰수
import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int,input().split()))

seq = {}

for i in arr:
    if i not in seq:
        seq[i] = 1
    else:
        seq[i] += 1

result = [-1] * n
stack = []

for i in range(n):
    num = arr[i]
    
    while stack and seq[stack[-1][0]] < seq[num]:
        element, idx = stack.pop()
        result[idx] = num
        
    stack.append((num, i))

print(*result)