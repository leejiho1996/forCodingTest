from collections import deque

def solution(people, limit):
    people.sort(reverse=True)
    que = deque(people)
    cnt = 0
    
    while que:
        cur = que.popleft()
        cnt += 1
        
        if que and que[-1] + cur <= limit:
            cur += que.pop()
    
    return cnt