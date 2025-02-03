def solution(phone_book):
    answer = True
    sett = set(phone_book)
    
    for i in phone_book:
        word = ""
        for j in i:
            word += j
            
            if word != i and word in sett:
                return False
        
    return answer