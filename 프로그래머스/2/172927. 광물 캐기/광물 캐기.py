def solution(picks, minerals):
    answer = 0
    cnt = 0
    dic = {
        "diamond" : 0,
        "iron" : 1,
        "stone" : 2
    }
    
    exhaust = {
        0 : (1, 1, 1),
        1 : (5, 1, 1),
        2 : (25, 5, 1)
    }
    minerals5 = []
    tool = sum(picks)*5
    while True:
        # 광물을 다켔거나 도구를 다 쓰면 break
        if cnt == len(minerals) or tool == 0:
            break
        # 5개씩 끊기
        mineral = [0,0,0]
        while True:
            m = minerals[cnt]
            mineral[dic[m]] += 1
            cnt += 1
            tool -= 1
            if cnt == len(minerals) or cnt % 5 == 0 or tool==0:
                minerals5.append(mineral)
                break
    # 다이아, 철, 돌멩이 순서로 정렬
    minerals5.sort(key = lambda x: (x[0], x[1], x[2]), reverse=True)
    
    for dia, iron, stone in minerals5:
        for j in range(3):
            if picks[j]:
                picks[j] -= 1
                answer += (exhaust[j][0] * dia + exhaust[j][1] * iron + exhaust[j][2] * stone)
                break
   
    return answer

