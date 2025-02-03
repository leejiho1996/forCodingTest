import heapq as hq

def solution(jobs):
    answer = 0
    jobs.sort() # 요청 시간 오름차순으로 정렬 
    que = [(jobs[0][1], jobs[0][0], 0)] # 첫 작업 삽입    
    time = que[0][1] # 첫 작업시작 시간은 첫 작업의 요청시간
    cnt = 1 # 작업 포인터
    
    while que:
        lead, call, order = hq.heappop(que)
        
        if call > time: 
            time = call
        
        time += lead
        answer += (time - call) # 반환시간을 더해준다
        
        # 현재 시간 이전에 요청이 들어온 작업을 대기큐에 넣어준다
        while cnt < len(jobs) and (not que or jobs[cnt][0] <= time):
            nCall, nLead = jobs[cnt]
            hq.heappush(que, (nLead, nCall, cnt))
            cnt += 1
    
    return answer // len(jobs)