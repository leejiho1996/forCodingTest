import sys
input = sys.stdin.readline

def cal(string, m):
    total = int(string[0])
    
    for i in range(2, m * 2 - 1, 2):
        if string[i - 1] == "-":
            total -= int(string[i])
        else:
            total += int(string[i])

    return total

def backtrack(r, c, cur, seq):

    if len(cur) > m * 2 - 1:
        return

    if len(cur) == m * 2 - 1:
        if cal(cur, m) == n:  
            print(1)
            for i, j in seq:
                print(i, j)
            exit()
        else:
            return
        
    for dx, dy in direc:
        nr, nc = r + dx, c + dy

        if nr < 0 or nc < 0 or nr >= 3 or nc >= 3:
            continue
        if (nr, nc) in visited:
            continue

        visited.add((nr, nc))
        backtrack(nr, nc, cur + graph[nr][nc], seq + [(nr, nc)])
        visited.remove((nr, nc))

n, m = map(int, input().split())
graph = []
direc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
dic = {}
visited = set()  

for i in range(3):
    graph.append(list(input().rstrip()))
    for j in range(3):
        dic[i * 3 + j] = (i, j)                    

for i in range(3):
    for j in range(3):
        if (i + j) % 2 == 1:
            continue
        visited.add((i, j))
        backtrack(i, j, graph[i][j], [(i, j)])
        visited.remove((i, j))

print(0)
