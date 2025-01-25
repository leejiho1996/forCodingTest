dices = []
result = []
maxx = 0    
visited = []

def makeAllCases(cnt, choices, total, sumList):
    if cnt == len(choices):
        sumList.append(total)
        return
        
    for i in range(6):
        makeAllCases(cnt+1, choices, total + choices[cnt][i], sumList)
 
def combination(A, B, diceA, diceB):
    global result
    global maxx
    
    total = 0
    sumA = []
    sumB = []
    
    makeAllCases(0, A, 0, sumA)
    makeAllCases(0, B, 0, sumB)
    
    sumA.sort()
    sumB.sort()
    
    for i in sumA:
        start = 0
        end = len(sumA) - 1
        
        while start <= end:
            mid = (start + end) // 2

            if sumB[mid] >= i:
                end = mid - 1
            else:
                start = mid + 1
        
        total += end
        
    if total > maxx:
        maxx = total 
        result = diceA
    
def dfs(start, cnt, diceCnt):
    if cnt == diceCnt//2:
        A = []
        diceA = []
        B = []
        diceB = []
    
        for i in range(diceCnt):
            if visited[i]:
                A.append(dices[i])
                diceA.append(i+1)
            else:
                B.append(dices[i])
                diceB.append(i+1)
                
        combination(A, B, diceA, diceB)
        return
    
    for i in range(start, diceCnt):  
        if visited[i]:
            continue
            
        visited[i] = 1
        dfs(i, cnt+1, diceCnt)
        visited[i] = 0
        
def solution(dice):
    global visited
    global dices
    global result
    
    answer = []
    dices = dice
    visited = [0] * len(dice)
    
    dfs(0, 0, len(dice))
    
    return result