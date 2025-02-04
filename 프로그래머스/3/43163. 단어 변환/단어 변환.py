from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    visited = {}
    visited[begin] = 99999
    
    for i in words:
        visited[i] = len(words)
    
    que = deque([(begin, 0)])
    
    while que:
        word, cnt = que.pop()
        
        if word == target:
            return cnt
        
        if visited[word] < cnt:
            continue
        else:
            visited[word] = cnt
            
        for j in words:
            unmatch = 0
            for k in range(len(word)):
                if word[k] != j[k]:
                    unmatch += 1

            if unmatch == 1 and visited[j] >= cnt + 1:
                que.append((j, cnt+1))

    return 0