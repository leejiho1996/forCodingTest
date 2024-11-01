from collections import deque
import heapq as hq

def solution(n, m, x, y, r, c, k):
    c -= 1
    r -= 1
    x -= 1
    y -= 1
    
    shortest = abs(c - x) + abs(r - y) # 출구까지 최단거리
    
    # 최단거리까지 가고 남은 이동횟수가 홀수이거나, 이동횟수보다 최단거리가 더 길면 불가능
    if (k - shortest) % 2 == 1 or k < shortest: 
        return "impossible"
    
    dic = {"l":(0, -1), "d":(1, 0), "u":(-1, 0), "r":(0, 1)}
    direc = ["d", "l", "r", "u"]
        
    que = deque([(x,y,0,"")])
    heap = [[] for _ in range(2501)]
    
    while que:
        cx, cy, cnt, word = que.popleft()
        
        if cnt == k and cx == r and cy == c:
            return word
        
        if cnt == k:
            continue
        
        for i in direc:
            nr, nc = dic[i]
            nx = cx + nr
            ny = cy + nc
            
            if not (0 <= nx < n) or not (0 <= ny < m):
                continue
                
            next_shortest = abs(r - nx) + abs(c - ny) # nx, ny를 갔을때 최단 거리
            rest = k - (cnt + 1) # 남은 이동 횟수
            
            if (rest - next_shortest) % 2 == 1 or rest < next_shortest: 
                continue
            
            if heap[cnt+1] and heap[cnt+1][0] < word+i:
                continue
            
            hq.heappush(heap[cnt+1], word+i)    
            que.append((nx, ny, cnt+1, word+i))
            
    return "impossible"