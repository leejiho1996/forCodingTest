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

        dx, dy = direc[i][0], direc[i][1]
        
        if direc[i][2] == 1:
            if red < blue:
                redAfter = moveBall(red, blue, dx, dy)
                blueAfter = moveBall(blue, redAfter, dx, dy)
            
            else:
                blueAfter = moveBall(blue, red, dx, dy)
                redAfter = moveBall(red, blueAfter, dx, dy)
        else:
            if red < blue:
                blueAfter = moveBall(blue, red, dx, dy)
                redAfter = moveBall(red, blueAfter, dx, dy)
            else:
                redAfter = moveBall(red, blue, dx, dy)
                blueAfter = moveBall(blue, redAfter, dx, dy)

        backtrack(cnt+1, redAfter, blueAfter, i)

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
