#7569
import sys
from collections import deque
all_fire_tomato = True
input = sys.stdin.readline
q = deque()
M, N, H = map(int, input().split())
result = 0
arr = []
for i in range(H):
    temp = []
    for j in range(N):
        zxc = list(map(int, input().split()))
        count = 0
        for num in zxc:
            if num == 0:
                all_fire_tomato = False
            elif num == 1:
                q.append((i,j,count))
            count +=1
        temp.append(zxc)
    arr.append(temp)


# 왼 오 앞 뒤 위 아래
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
    global result


    while q:
        c, b, a = q.popleft()

        for i in range(6):
            nx = a + dx[i]
            ny = b + dy[i]
            nz = c + dz[i]

            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H:
                if arr[nz][ny][nx] == 0:
                    arr[nz][ny][nx] = arr[c][b][a] + 1
                    temp = [nz, ny, nx]
                    q.append(temp)
                    if result < arr[nz][ny][nx]:
                        result= arr[nz][ny][nx]

if all_fire_tomato:
    print(0)
else:
    bfs()
    for k in range(H):
        for i in range(N):
            for j in range(M):
                if arr[k][i][j] == 0:
                    print(-1)
                    sys.exit()
    print(result-1)