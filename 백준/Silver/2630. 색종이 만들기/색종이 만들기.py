# 색종이 만들기
import sys
input = sys.stdin.readline

n = int(input())

paper = [list(map(int,input().split())) for _ in range(n)]

blue = 0
white = 0

def divide(s_r, s_c , num):
    global blue
    global white
    s = 0

    for i in range(s_r, s_r+num):
        for j in range(s_c, s_c+num):
            s += paper[i][j]
    
    if s == num**2:
        blue += 1
        return
    if s == 0:
        white += 1
        return
    if num == 1:
        return
    
    next_size = num//2
    for n_r, n_c in [(0,0), (0, next_size), (next_size, 0), (next_size, next_size)]:
        divide(s_r+n_r, s_c+n_c, next_size)
        
    
divide(0, 0, n)

print(white)
print(blue)