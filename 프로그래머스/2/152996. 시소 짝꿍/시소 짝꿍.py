def solution(weights):
    answer = 0
    
    dic = {}
    
    for i in weights:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    
    nums = list(dic.keys())
    length = len(nums)
    
    for i in range(length):
        num = nums[i]
        answer += (dic[num] * (dic[num]-1)) // 2 # 같은 경우 처리 
        
        if num * (4/3) in dic:
            answer += dic[num] * dic[num*(4/3)]
        
        if num * (3/2) in dic:
            answer += dic[num] * dic[num*(3/2)]
        
        if num * (2) in dic:
            answer += dic[num] * dic[num*(2)]
        

    return answer