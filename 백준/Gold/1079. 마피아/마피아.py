# 마피아
import sys
input = sys.stdin.readline

N = int(input())
guilty = list(map(int,input().split()))
graph = []
dead = [0] * N
result = 0

for i in range(N):
    graph.append(list(map(int,input().split())))

E = int(input())

stack = [(N, 0, 0, guilty)]

while stack:
    alive, dead, day, guilties = stack.pop()
    
    # 낮일 때
    if alive % 2 == 1:
        maxx = -1
        max_idx = -1
        
        for i in range(N):
            if dead & (1 << i):
                continue

            if maxx < guilties[i]:
                maxx = guilties[i]
                max_idx = i
        
        if max_idx == E:
            result = max(result, day)
        else:
            stack.append((alive-1, dead | (1 << max_idx), day, guilties.copy()))
            
    # 밤일 때
    else:
        for i in range(N):
            if dead & (1 << i) or i == E:
                continue

            tmp = guilties.copy()

            for j in range(N):
                tmp[j] += graph[i][j]
                
            stack.append((alive-1, dead | (1 << i) , day+1, tmp))

print(result)
        
