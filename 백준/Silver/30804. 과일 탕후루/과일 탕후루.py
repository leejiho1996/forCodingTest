# 과일 탕후루
import sys
input = sys.stdin.readline

n = int(input())
tang = list(map(int,input().split()))
stack = []
max_length = [0] * n
types = set()
result = 0

for i in range(n):
    cur = tang[i]
    types.add(cur)

    if len(types) > 2:
        cnt = 0
        while stack and stack[-1] == tang[i-1]:
            stack.pop()
            cnt += 1
            
        types = {cur, tang[i-1]}
        stack = [cur]
        max_length[i] = cnt + 1
    else:
        max_length[i] = max_length[i-1] + 1
        stack.append(cur)

print(max(max_length))
