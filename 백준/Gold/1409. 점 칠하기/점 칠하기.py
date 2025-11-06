import sys

input = sys.stdin.readline

ang = [0] * 360

N = int(input())

for i in range(N):
    ang[int(input())] = 1

result = 0
for d in range(1, 181):
    cnt = 0
    visited = [0] * 360
    for j in range(360):
        
        if visited[j] or not ang[j]:
            continue

        tmp = 0

        # 시계방향으로 체크
        x = j
        while ang[x] and not visited[x]:
            visited[x] = 1
            tmp += 1
            x = (x+d) % 360

        # 반시계방향으로 체크
        x = (j-d) % 360
        while ang[x] and not visited[x]:
            visited[x] = 1
            tmp += 1
            x = (x-d) % 360

        cnt += tmp//2
        
    result = max(result, cnt)

print(result*2)
