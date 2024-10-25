# 쿠키의 신체 측정
import sys
input = sys.stdin.readline

n = int(input())
is_head = False
is_heart = False

graph = []
for i in range(n):
    line = input().rstrip()
    
    for j in range(n):
        if line[j] == "*" and not is_head:
            is_head = True
            heart = (i+2, j+1)
            
    graph.append(line)
    
left_arm = 1
right_arm = 1
left_leg = 1
right_leg = 1
waist = 1
s, e = heart[0] - 1, heart[1] - 1



while True:
    if e-left_arm < 0:
        left_arm -= 1
        break
    
    if graph[s][e-left_arm] == "*":
        left_arm += 1
    else:
        left_arm -= 1
        break
    
while True:
    if e+right_arm >= n:
        right_arm -= 1
        break
    
    if graph[s][e+right_arm] == "*":
        right_arm += 1
        continue
    else:
        right_arm -= 1
        break
    
while True:
    if s+waist >= n:
        waist -= 1
        break
    if graph[s+waist][e] == "*":
        waist += 1
    else:
        waist -= 1
        break

while True:
    if s+waist+left_leg >= n:
        left_leg -=1
        break
    
    if graph[s+waist+left_leg][e-1] == "*":
        left_leg += 1
    else:
        left_leg -= 1
        break

while True:
    if s+waist+right_leg >= n:
        right_leg -=1
        break

    if graph[s+waist+right_leg][e+1] == "*":
        right_leg += 1
    else:
        right_leg -= 1
        break

print(heart[0], heart[1])
print(left_arm, right_arm, waist, left_leg, right_leg)
        
