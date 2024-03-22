import math

def solution(r1, r2):
    ans = 0
    for i in range(1, r2+1):
        ymax = int(math.sqrt(r2**2-i**2))
        if i>r1:
            ymin = 0
        else:
            ymin = math.ceil(math.sqrt(r1**2-i**2))
        ans += ymax-ymin+1
    return ans*4
