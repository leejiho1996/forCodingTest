# RGB거리 (dp)
import sys
input = sys.stdin.readline

n = int(input())

dp_red = [0] * n; dp_green = [0] * n; dp_blue = [0] * n


for i in range(n):
    red, green, blue = map(int, input().split())
    if i == 0:
        dp_red[0] = red
        dp_green[0] = green
        dp_blue[0] = blue
        continue
    dp_red[i] = min(dp_green[i-1] + red, dp_blue[i-1] + red)
    dp_green[i] = min(dp_red[i-1] + green, dp_blue[i-1] + green)
    dp_blue[i] = min(dp_green[i-1] + blue, dp_red[i-1] + blue)
    
print(min(dp_red[-1], dp_green[-1], dp_blue[-1]))