def dfs(cnt, users, emoticons, sale_percent):
    if cnt == len(emoticons):
        total = 0
        sub = 0
        for dis, lim in users:
            part = 0
            for j in range(len(emoticons)):
                if sale_percent[j] < dis:
                    continue
                part += emoticons[j] * (100 - sale_percent[j]) // 100
            if part >= lim:
                sub += 1
            else:
                total += part           
        return [sub, total]
    
    lis = []
    for i in [10, 20, 30, 40]:
        sale_percent[cnt] = i
        lis.append(dfs(cnt+1, users, emoticons, sale_percent))
        
    lis.sort(key = lambda x:(-x[0], -x[1]))
    return lis[0]

def solution(users, emoticons):
    answer = dfs(0, users, emoticons, [0] * len(emoticons))
    return answer