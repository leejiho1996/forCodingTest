a, b = map(int,input().split())

c = []

for i in range(1,a+1):
    c.append(str(i))


def backtrack(n, word):
    if len(word) == b:
        
        return print(*[int(i) for i in list(word)])

    for i in range(len(n)):
        if n[i] != 'used': 
            nword = word + str(n[i])
            n[i] = 'used' 
            if backtrack(n, nword):
                return True

            n[i] = nword[-1]
    
backtrack(c, '')