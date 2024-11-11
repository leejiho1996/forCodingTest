def yaksoo(num):
    yak = set()
    
    for i in range(2, int(num**(0.5))+1):
        if num % i == 0:
            yak.add(i)
            yak.add(num // i)
    yak.add(num)
    
    return yak

def cal_max(pos, A, B):
    max_num = 0
    
    for i in pos:
        checkA = True
        checkB = True
        
        for j in range(len(A)):
            if A[j] % i != 0:
                checkA = False
                break
            
            if B[j] % i == 0:
                checkB = False
                break
        
        if not checkA or not checkB:
            continue
            
        max_num = max(max_num, i)
    
    return max_num


def solution(arrayA, arrayB):    
    arrayA.sort()
    arrayB.sort()
    
    minA = arrayA[0]
    minB = arrayB[0]

    maxx = 0
    
    posA = yaksoo(minA)
    posB = yaksoo(minB)
    
    maxx = max(cal_max(posA, arrayA, arrayB), cal_max(posB, arrayB, arrayA))
    
    return maxx