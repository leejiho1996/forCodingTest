def solution(n, computers):
    visited = [0] * n
    cnt = 0 
    
    for i in range(n):
        if visited[i]:
            continue
        
        cnt += 1
        stack = [i]
        
        while stack:
            cur = stack.pop()
            
            if visited[cur]:
                continue
            else:
                visited[cur] = 1
                
            for j in range(n):
                if not computers[cur][j]:
                    continue
                elif cur == j or visited[j]:
                    continue
                else:
                    stack.append(j)

    return cnt