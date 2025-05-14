# 지연 평가
import sys
input = sys.stdin.readline

Q = int(input())
small = 1
add = 0
multi = 1

for i in range(Q):
    cmd = list(map(int,input().split()))

    if cmd[0] == 3:
        print(small*multi+add)
    elif cmd[0] == 1:
        add *= cmd[1]
        multi *= cmd[1]
    elif cmd[0] == 0:
        add += cmd[1]
    else:
        small += cmd[1]
