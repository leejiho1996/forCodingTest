# 열쇠
import sys
input = sys.stdin.readline
from collections import deque

direc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            
test = int(input())

for t in range(test):
    h, w = map(int,input().split())
    graph = []
    visited = [[0] * w for _ in range(h)]
    keySet = set() # 열쇠를 저장할 set
    result = 0

    alphabet = {} # 알파벳별 멈춘 좌표를 저장할 딕셔너리
    for i in range(26):
        alphabet[chr(65+i)] = []

    for i in range(h):
        graph.append(list(input().rstrip()))

    keys = input().rstrip()
    if keys != "0":
        for i in keys:
            keySet.add(i)

    que = deque([]) # 출입 가능한 입구를 담을 큐

    for i in range(h):
        if graph[i][0] != "*":
            que.append((i, 0))

        if graph[i][w-1] != "*":
            que.append((i, w-1))

    for i in range(w):
        if graph[0][i] != "*":
            que.append((0, i))

        if graph[h-1][i] != "*":
            que.append((h-1, i))
            
    while que:
        r, c = que.popleft()
        word = graph[r][c]
        
        # 현재 지역이 문이고, 통과할수 없는 문이라면 해당 알파벳의 스택에 담아둔다
        if word in alphabet and word.lower() not in keySet: 
            alphabet[word].append((r, c))
            continue
        
        if visited[r][c]:
            continue
        else:
            visited[r][c] = 1

        # 현재 지역이 열쇠일때
        if word.islower():
            # 열쇠셋에 담아주고 해당 문에서 멈춘 좌표가 있다면 큐에 담아준다
            keySet.add(word) 
            stack = alphabet[word.upper()] 
            while stack:
                que.append(stack.pop())         

        if word == "$": # 문서라면 카운트 +1 
            result += 1
 
        for dx, dy in direc:
            nr, nc = r + dx, c + dy

            if nr < 0 or nc < 0 or nr >= h or nc >= w:
                continue
            elif visited[nr][nc] or graph[nr][nc] == "*":
                continue
            else:
                que.append((nr, nc))
                
    print(result)
    
