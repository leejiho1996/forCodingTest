import heapq

def solution(n, k, enemy):
    total = sum(enemy)
    
    if n >= total:
        return len(enemy)
    
    answer = 0
    que = []
    for i in enemy:
        if n - i  >= 0: # 가능하다면 힙에 해당 숫자를 넣고 진행, 최대힙이어야하므로 음수로 넣는다
            heapq.heappush(que, -i)
            answer += 1
            n -= i
            continue
        
        if k: # 무적권이 있을때 
            if que and -que[0] > i: # 큐의 최대값이 현재값보다 크다면 최대값에 무적권 사용
                n += (-heapq.heappop(que) - i)
                k -= 1
                answer += 1
                heapq.heappush(que, -i)
            elif (que and -que[0] <= i) or len(que) == 0: # 큐의 최대값이 작거나 큐가 비었다면 현재값에 무적권 사용
                k -= 1
                answer += 1
        else:
            break    
                
    return answer