# 영재의 산책
import sys
input = sys.stdin.readline

V, M, T = map(int,input().split())

T -= 1
X = 0
Y = V # 처음은 북쪽으로 이동
direc = 0 # 처음 방향은 북

# 북 0 동 1 남 2 서 3
pos = {0 : (0, 1), 1 : (1, 0), 2: (0, -1), 3 : (-1, 0)}
cycle = []

while True:
    V = (V * M) % 10

    if V in cycle:
        break
    else:
        cycle.append(V)

# 한바퀴 돌았을 때 이동거리 계산 및 저장
dx = 0
dy = 0
move = [(0, 0)]

for i in range(4):
    direc = (direc+1) % 4

    dx += pos[direc][0] * cycle[i % len(cycle)]
    dy += pos[direc][1] * cycle[i % len(cycle)]
    # 배열에 저장
    move.append((dx, dy))
    
X += dx * (T // 4)
Y += dy * (T // 4)

print(X + move[T % 4][0], Y + move[T % 4][1])
