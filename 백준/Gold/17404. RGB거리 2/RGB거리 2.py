# RGB거리 2
import sys
input = sys.stdin.readline

n = int(input())

red = [[-1, -1, -1] for _ in range(n)] 
green = [[-1, -1, -1] for _ in range(n)]
blue = [[-1, -1, -1] for _ in range(n)]

# color[i][n] => color로 i번째 색칠할때 n번째는 시작한 color 
for i in range(n):
    r, g, b = map(int,input().split())

    if i == 0:
        red[i] = [r, r, r]
        green[i] = [g, g, g]
        blue[i] = [b, b, b]
        continue

    if i == 1:
        red[i] = [float('inf'), green[i-1][0] + r, blue[i-1][0] + r]
        blue[i] = [red[i-1][0] + b, green[i-1][0] + b, float('inf')]
        green[i] = [red[i-1][0] + g, float('inf'), blue[i-1][0] + g]
        continue

    for j in range(3):
        red[i][j] = min(blue[i-1][j] + r, green[i-1][j] + r)
        green[i][j] = min(red[i-1][j] + g, blue[i-1][j] + g)
        blue[i][j] = min(green[i-1][j] + b, red[i-1][j] + b)
        
print(min(min(red[-1][1], red[-1][2]),
          min(green[-1][0], green[-1][2]),
          min(blue[-1][0], blue[-1][1])
          ))
    
    
