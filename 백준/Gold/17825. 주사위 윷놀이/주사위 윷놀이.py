# 주사위 윷놀이
import sys
input = sys.stdin.readline

def checkSame(r, c, idx):
    for i in range(4):
        if i == idx:
            continue

        if pieces[i][0] == r and pieces[i][1] == c:
            return 0

    return 1

def move(r, c, cur):
    cnt = dices[cur]

    if r == 0 and c == 5:
        r = 1
        c = 0
    elif r == 0 and c == 10:
        r = 2
        c = 0
    elif r == 0 and c == 15:
        r = 3
        c = 0

    lim = len(graph[r])
     
    if c + cnt >= lim:
        return (-1, -1, 0)

    if r > 0 and graph[r][c+cnt] in dic:
        return dic[graph[r][c+cnt]]
    else:
        return (r, c + cnt, graph[r][c+cnt])

def brute(cur, total):

    global maxx

    maxx = max(maxx, total)
    
    if cur == 10:
        return

    for i in range(4):
        prevR, prevC = pieces[i]
        check = 1
        
        if prevR == -1:
            continue
        
        nextR, nextC, points = move(prevR, prevC, cur)
        
        if nextR != -1:
            check = checkSame(nextR, nextC, i)
            
        if check:
            pieces[i][0], pieces[i][1] = nextR, nextC
            brute(cur+1, total+points)
            pieces[i][0], pieces[i][1] = prevR, prevC        

dices = list(map(int,input().split()))

graph = []
graph.append([i for i in range(0, 41, 2)])
graph.append([10, 13, 16, 19, 25, 30, 35, 40])
graph.append([20, 22, 24, 25, 30, 35, 40])
graph.append([30, 28, 27, 26, 25, 30, 35, 40])
graph.append([25, 30, 35, 40])

dic = {25 : (4, 0, 25), 30: (4, 1, 30), 35: (4, 2, 35), 40:(0, 20, 40)}

maxx = 0
pieces = [[0, 0], [0, 0], [0, 0], [0, 0]]
brute(0, 0)

print(maxx)
