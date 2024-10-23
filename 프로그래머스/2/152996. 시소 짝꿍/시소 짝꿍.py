def match(num, opp):
    seats = (2,3,4)
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            if num * seats[i] == opp * seats[j]:
                return 1
    return 0
    
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
        for j in range(i+1, length):
            if i == j:
                continue
            opp = nums[j]
            
            if match(num, opp):
                answer += 1 * (dic[num] * dic[opp])

    return answer