import heapq

def solution(genres, plays):
    answer = []
    dic = {}
    cntDic = {}
    
    length = len(plays)
    
    for i in range(length):
        genre = genres[i]
        play = plays[i]
        
        if genre not in dic:
            dic[genre] = [(-play, genre, i)]
            cntDic[genre] = play
        else:
            heapq.heappush(dic[genre], (-play, genre, i))
            cntDic[genre] += play
            
    genres = list(set(genres))
    genres.sort(key = lambda x:-cntDic[x])
    
    for i in genres:
        for j in range(2):
            answer.append(heapq.heappop(dic[i])[2])
            
            if len(dic[i]) == 0:
                break
        
    return answer