# 숫자 할당
import sys
input = sys.stdin.readline

def backtrack(r, c):

    global result
    
    if r == 5:
        result +=1
        return

    if r + c == 6 or (r == 1 and c == 4):
        nr = r + 1
        nc = 1
    else:
        nr = r
        nc = c + 1

    for i in range(1, 14):
        if visited[i]:
            continue

        if nc == 1 and row_sum[r] + i != row[r]:
            continue

        if r == 4 or r + c == 6:
            if col_sum[c] + i != col[c]:
                continue

        row_sum[r] += i
        col_sum[c] += i
        visited[i] = 1
        
        backtrack(nr, nc)
        
        row_sum[r] -= i
        col_sum[c] -= i
        visited[i] = 0
    

A, B, C, D, E, F, G, H = map(int,input().split())

row = [0] * 5
col = [0] * 5

col[1] = A; col[2] = B; col[3] = C; col[4] = D;
row[1] = E; row[2] = F; row[3] = G; row[4] = H;

row_sum = [0] * 5
col_sum = [0] * 5
visited = [0] * 14

result = 0

backtrack(1, 1)

print(result)
