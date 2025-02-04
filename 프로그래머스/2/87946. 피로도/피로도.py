result = 0
visited = []

def backtrack(cnt, dungeons, k):
    global result
    result = max(result, cnt)
    
    for i in range(len(dungeons)):
        need = dungeons[i][0]
        consume = dungeons[i][1]
        
        if visited[i] or k - need < 0:
            continue
        
        visited[i] = 1
        backtrack(cnt+1, dungeons, k - consume)
        visited[i] = 0
        

def solution(k, dungeons):
    global visited
    visited = [0] * len(dungeons)
    backtrack(0, dungeons, k)
    return result