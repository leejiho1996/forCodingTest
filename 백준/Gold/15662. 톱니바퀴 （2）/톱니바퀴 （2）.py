# 톱니바퀴(2)
import sys
input = sys.stdin.readline

def changeLeft(start, turn):

    prev = wheels[start]
    
    for i in range(start-1, -1, -1):
        # 똑같은 극이 맞닿아있다면 회전 x
        if prev[6] == wheels[i][2]:
            break

        prev = wheels[i] # 이동 전의 정보를 저장
        
        if turn == 1: # 옆의 톱니가 시계 방향 이동했을 때
            wheels[i] = wheels[i][1:] + wheels[i][0]
        else:
            wheels[i] = wheels[i][-1] + wheels[i][0:-1]

        # 방향을 반대로
        turn = -turn

def changeRight(start, turn):

    prev = wheels[start]
    
    for i in range(start+1, T):
        # 똑같은 극이 맞닿아있다면 회전 x
        if prev[2] == wheels[i][6]:
            break

        prev = wheels[i] # 이동 전의 정보를 저장
        
        if turn == 1: # 옆의 톱니가 시계 방향 이동했을 때
            wheels[i] = wheels[i][1:] + wheels[i][0]
        else:
            wheels[i] = wheels[i][-1] + wheels[i][0:-1]

        turn = -turn
    
T = int(input())
wheels = []

for i in range(T):
    wheels.append(input().rstrip())

K = int(input())

for i in range(K):
    start, turn = map(int,input().split())
    start -= 1
    # 양옆의 톱니들을 회전시킨다
    changeLeft(start, turn)
    changeRight(start, turn)

    # 현재 톱니바퀴도 회전
    if turn == 1:
        wheels[start] = wheels[start][-1] + wheels[start][0:-1]
    else:
        wheels[start] = wheels[start][1:] + wheels[start][0]

result = 0
for i in range(T):
    if wheels[i][0] == '1':
        result += 1

print(result)


