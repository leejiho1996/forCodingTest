def solution(scores):
    answer = 0
    length = len(scores)
    score = [(scores[i][0] + scores[i][1], scores[i][0], scores[i][1]) for i in range(length)]

    wanho = score[0]
    score.sort(key=lambda x : (-x[1], -x[2]))
    available = []
    
    mx_score = [-1] * 100001
    prev = score[0][1] 
    cur_mx = score[0][2] # 내림차순 정렬이기 때문에 첫번째 수는 무조건 인센티브를 받는다
    
    for i in range(length):
            
        if score[i][1] == prev: 
            if score[i][2] >= mx_score[prev]: # 현재와 이전이 같고 앞에 나온 수보다 크다면 가능
                available.append(score[i])
        else:
            if score[i][2] >= cur_mx: # 현재와 이전이 다르고 앞에 나온수보다 크다면 가능
                available.append(score[i])
            
            prev = score[i][1] 
            mx_score[prev] = cur_mx # 이전값까지의 최대 숫자를 갱신
            cur_mx = max(cur_mx, score[i][2]) # 현재까지의 최대 숫자를 갱신
            

    available.sort(reverse=True)
    
    if wanho in available:
        return available.index(wanho) + 1
    else:
        return -1