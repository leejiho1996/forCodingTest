# 컨베이어 벨트 위의 로봇
import sys
input = sys.stdin.readline

n, k = map(int,input().split())
dura = list(map(int,input().split()))
robot = [0] * n
zero = 0

cnt = 0
while True:
    cnt += 1

    dura = [dura[-1]] + dura[:-1] # 벨트 이동
    robot = [0] + robot[0:-1]
    
    for i in range(n-1, -1, -1): # 로봇 이동
        if robot[i] == 0:
            continue

        if i == n - 1: # 로봇이 벨트 끝에 있다면 무조건 이동 가
            robot[i] = 0
            continue

        if  dura[i+1] > 0 and robot[i+1] == 0:
            robot[i] = 0
            robot[i+1] = 1
            dura[i+1] -= 1

            if dura[i+1] == 0:
                zero += 1

    if dura[0]: # 로봇 올리기
        robot[0] = 1
        dura[0] -= 1
        
        if dura[0] == 0:
            zero += 1

    if zero >= k:
        break

print(cnt)
    
