def parse(expression):
    parts, result = expression.split(" = ")
         
    if "+" in parts:
        left, right = parts.split(" + ")
        operation = "+"
    else:
        left, right = parts.split(" - ")
        operation = "-"

    return (left, right, result, operation)

def numeralChange(n, num):
    result = ""
    while num >= n:
        result += str(num % n)
        num //= n
        
    result += str(num)
    return int(result[::-1])

def solution(expressions):
    answer = []
    xs = []
    complete = []
    candi = []
    
    maxx = 0
    for i in expressions:
        if i[-1] == "X":
            xs.append(i)
        else:
            complete.append(parse(i))
        
        for j in range(8, 1, -1): # 1차적으로 가능한 숫자 계산
            if j < maxx:
                break
                
            if str(j) in i and j > maxx:
                maxx = j
            
    num_range = [i for i in range(maxx+1, 10)]
    
    for i in num_range:
        check = True
        for l, r, res, op in complete:
            try:
                left = int(l, i)
                right = int(r, i)
                result = int(res, i)
            except:
                check = False
                break
            
            if op == "-" and left - right != result:
                check = False
                break
            elif op == "+" and left + right != result:
                check = False
                break
        
        if check:
            candi.append(i)
    
    for i in xs:
        l, r, res, op = parse(i)
        possible = set()
        for j in candi:
            try:
                left = int(l, j)
                right = int(r, j)
            except:
                continue
            
            if op == "-":
                possible.add(numeralChange(j, left - right))
            else:
                possible.add(numeralChange(j, left + right))
        
        
        if len(possible) >= 2:
            result = "?"
        else:
            result = str(possible.pop())
            
        answer.append(l + " " + op + " " + r + " = " + result)
    return answer