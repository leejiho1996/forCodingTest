def cal(h, m, s):
    result = 2 * (60*h + m)
    
    hour = (30 * h + (1/120) * (s + m * 60)) % 360
    minute = 6 * m + (1/10) * s
    second = 6 * s
    
    if second >= minute:
        result += 1
    
    if second >= hour:
        result += 1
        
    result -= 1 # 0시 0분 0초
    result -= h # 59분 -> 00 분 될 때, 즉 매 한시간마다 안겹침
    
    if h >= 12: # 11시 59분 -> 12시가 될 때 시침과 안겹치고, 12시 정각일때는 시침 분침 모두와 겹쳐서 -2
        result -= 2

    return result
    
def solution(h1, m1, s1, h2, m2, s2):
    
    answer = cal(h2, m2, s2) - cal(h1, m1, s1)

    if (h1 == 0 or h1 == 12) and m1 == 0 and s1 == 0:
        answer += 1
        
    return answer