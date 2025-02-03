from collections import deque

def solution(priorities, location):
    answer = 0
    que = deque([])
    
    for i in range(len(priorities)):
        que.append((i, priorities[i]))
    
    priorities.sort()
    
    cnt = 0
    while que:
        idx, cur = que.popleft()
        
        if cur != priorities[-1]:
            que.append((idx, cur))
        else:
            if idx == location:
                return cnt + 1
            
            cnt += 1
            priorities.pop()
    