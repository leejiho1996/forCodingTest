# 구슬 탈출2
import sys
input = sys.stdin.readline

def backtrack(cnt, red, blue, last):
    global result
    
    if cnt > 10:
        return

    if red == end and blue == end:
        return
    elif blue == end:
        return
    elif red == end:
        result = min(result, cnt)
        return

    for i in range(4):
        if i == last:
            continue
        
        redBefore = red
        blueBefore = blue
        redAfter, blueAfter = move(red, blue, direc[i][0], direc[i][1], direc[i][2])

        backtrack(cnt+1, redAfter, blueAfter, i)

def move(red, blue, dx, dy, reverse):

    # 왼쪽, 위로 이동은 위치가 작은 쪽이 먼저 이동해야함
    if reverse == 1:
        if red < blue:
            red = moveBall(red, blue, dx, dy)
            blue = moveBall(blue, red, dx, dy)
            
        else:
            blue = moveBall(blue, red, dx, dy)
            red = moveBall(red, blue, dx, dy)
            

    # 아래, 오른쪽 이동은 큰 쪽이 먼저 이동해야함
    else:
        if red < blue:
            blue = moveBall(blue, red, dx, dy)
            red = moveBall(red, blue, dx, dy)
        else:
            red = moveBall(red, blue, dx, dy)
            blue = moveBall(blue, red, dx, dy)

    return (red, blue)

def moveBall(ball1, ball2, dx, dy):
    r, c = ball1
    
    while True:
        if (r+dx, c+dy) == end:
            return(r+dx, c+dy)
                
        elif graph[r+dx][c+dy] == "#" or (r+dx, c+dy) == ball2:
            return (r, c)
            break

        r += dx
        c += dy

    return (r, c)

n, m = map(int,input().split())
result = 1000
graph = []

# 아래, 위, 오른쪽, 왼쪽 이동
direc = [(1, 0, 0), (-1, 0, 1), (0, 1, 0), (0, -1, 1)]

for i in range(n):
    row = list(input().rstrip())
    graph.append(row)

    for j in range(m):
        if row[j] == "R":
            red = (i, j)
        elif row[j] == "B":
            blue = (i, j)
        elif row[j] == "O":
            end = (i, j)

backtrack(0, red, blue, -1)

if result == 1000:
    print(-1)
else:
    print(result)
