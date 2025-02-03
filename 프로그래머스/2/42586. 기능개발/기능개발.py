def solution(progresses, speeds):
    answer = []
    pointer = 0
    length = len(progresses)
    
    while pointer < length:
        while progresses[pointer] < 100:
            for i in range(length):
                progresses[i] += speeds[i]
        
        cnt = 0
        while pointer < length and progresses[pointer] >= 100:
            cnt += 1
            pointer += 1
        
        answer.append(cnt)
        
    return answer