#체스판 다시 칠하기

a, b = map(int, input().split())
board = []
chess_w = []
chess_b = []
mn = a*b
for i in range(a):
    board.append(list(input()))

for i in range(8):
    if i % 2 == 0:
        chess_w.append(list('WBWBWBWB'))
        chess_b.append(list('BWBWBWBW'))
    else:
        chess_w.append(list('BWBWBWBW'))
        chess_b.append(list('WBWBWBWB'))
            
for i in range(a-7):
    
    for j in range(b-7):
        chess = []
        mn_w = 0
        mn_b = 0
        for k in range(8):
            chess.append(board[i+k][j:8+j])
    
        for q in range(8):
            for w in range(8):
                if chess[q][w] != chess_w[q][w]:
                    mn_w += 1
                if chess[q][w] != chess_b[q][w]:
                    mn_b += 1
        mnn = min(mn_w, mn_b)
        if mnn < mn:
            mn = mnn

print(mn)
