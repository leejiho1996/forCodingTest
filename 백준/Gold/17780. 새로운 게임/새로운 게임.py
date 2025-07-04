# 새로운 게임
import sys
input = sys.stdin.readline

def isFinish(idx, cnt):
    if len(child[idx]) >= 4:
        print(cnt)
        exit()

def moveWhite(idx, r, c, nr, nc, direc):
    
    if pos[nr][nc] != -1:
        for i in child[idx]:
            child[pos[nr][nc]].append(i)
            pieces[i] = (i, nr, nc, pieces[i][3]) 

        child[idx] = []

        isFinish(pos[nr][nc], cnt)
    else: 
        for i in child[idx]:
            pieces[i] = (i, nr, nc, pieces[i][3])

        pos[nr][nc] = idx

    pos[r][c] = -1
        
def moveRed(idx, r, c, nr, nc, direc):
         
    if pos[nr][nc] != -1: 
        for i in range(len(child[idx])-1, -1, -1): 
            cur = child[idx][i]
            child[pos[nr][nc]].append(child[idx][i])
            pieces[cur] = (cur, nr, nc, pieces[cur][3]) 

        isFinish(pos[nr][nc], cnt) 
        
        child[idx] = []
    else: 
        if len(child[idx]) > 1:
            for i in range(len(child[idx])-1, -1, -1): 
                cur = child[idx][i]
                child[child[idx][-1]].append(cur)
                pieces[cur] = (cur, nr, nc, pieces[cur][3]) 
            
            pos[nr][nc] = child[idx][-1] 
            child[idx] = []
        else:
            pieces[idx] = (idx, nr, nc, pieces[idx][3])
            pos[nr][nc] = idx

    pos[r][c] = -1

def moveBlue(idx, r, c, nr, nc, direc):

    if direc % 2 == 1:
        reverse = direc + 1
    else:
        reverse = direc - 1

    pieces[idx] = (idx, r, c, reverse)
    
    if nr < 0 or nc < 0 or nr >= N or nc >= N or board[nr][nc] == 2: 
        pass
    elif board[nr][nc] == 1:
        moveRed(idx, r, c, nr, nc, direc)
    else:
        moveWhite(idx, r, c, nr, nc, direc)

N, K = map(int,input().split())
board = []
pos = [[-1] * N for _ in range(N)]
pieces = []
child = [[i] for i in range(K)]
move = {1 : (0, 1), 2 : (0, -1), 3 : (-1, 0), 4 : (1, 0)}

for i in range(N):
    board.append(list(map(int,input().split())))

for idx in range(K):
    r, c, direc = map(int,input().split())
    pos[r-1][c-1] = idx
    pieces.append((idx, r-1, c-1, direc))

cnt = 1
while cnt < 1000:
    for i in range(K):
        idx, r, c, direc = pieces[i]

        if len(child[idx]) == 0:
            continue

        nr, nc = r + move[direc][0] , c + move[direc][1]

        if nr < 0 or nc < 0 or nr >= N or nc >= N or board[nr][nc] == 2:
            if direc % 2 == 1:
                ndirec = direc + 1
            else:
                ndirec = direc - 1

            nr, nc = r + move[ndirec][0], c + move[ndirec][1]
            moveBlue(idx, r, c, nr, nc, direc)          
        elif board[nr][nc] == 0:
            moveWhite(idx, r, c, nr, nc, direc)
        else:
            moveRed(idx, r, c, nr, nc, direc)

    cnt += 1

print(-1)
