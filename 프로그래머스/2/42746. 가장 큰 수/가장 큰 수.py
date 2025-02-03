def solution(numbers):
    answer = ''
    word = []
    
    numbers.sort(key = lambda x : str(x) * 3, reverse = True)
    
    for i in numbers:
        answer += str(i)
    
    if int(answer) == 0:
        return "0"
    else:
        return answer
    