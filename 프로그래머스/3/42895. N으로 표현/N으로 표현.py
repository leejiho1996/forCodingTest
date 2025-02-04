def solution(N, number):
    if number == 1:
        return 1
    
    dp = [[]]
    
    for i in range(1, 9):
        sett = set()
        sett.add(int(str(N)*i))
        
        for j in range(1, i):
            for op1 in dp[j]:
                for op2 in dp[i-j]:
                    sett.add(op1 + op2)
                    sett.add(op1 - op2)
                    sett.add(op1 * op2)
                    if op2 != 0:
                        sett.add(op1 // op2)
                        
        if number in sett:
            return i
        dp.append(sett)
    return -1