import sys
input = sys.stdin.readline

n = int(input())
buildings = list(map(int,input().split()))

def cal_equation(x1, y1, x2, y2):
    gradient = (y1 - y2) / (x1 - x2)
    c = -gradient * x1 + y1
    return (gradient, c)

maxx = 0
for i in range(n):
    building = buildings[i]
    cnt = 0

    for j in range(0, i):
        gradient, c = cal_equation(i, building, j, buildings[j])

        possible = True
        for k in range(j+1, i):
            if gradient * k + c <= buildings[k]:
                possible = False
                break

        if possible:
            cnt += 1
        
    for j in range(n-1, i , -1):
        gradient, c = cal_equation(i, building, j, buildings[j])

        possible = True
        for k in range(j-1, i, -1):
            if gradient * k + c <= buildings[k]:
                possible = False
                break

        if possible:
            cnt += 1
            
    maxx = max(maxx, cnt)
    
print(maxx)
