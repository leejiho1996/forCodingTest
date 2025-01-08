# 과일 탕후루
import sys
input = sys.stdin.readline

n = int(input())
tang = list(map(int,input().split()))
start = -1
types = set()
result = 0

for i in range(n):
    cur = tang[i]
    types.add(cur)

    if len(types) > 2:
        start = i-2
        while tang[start] == tang[i-1]:
            start -= 1
            
        types = {cur, tang[i-1]}
        result = max(result, i - start)
    else:
        result = max(result, i-start)

print(result)
