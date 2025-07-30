# HTML
words = []

while True:
    try:
        line = input()
    except EOFError:
        break

    for i in line.rstrip().split():
        words.append(i)

result = ""
curCnt = 0

for i in words:

    if i == "<br>":
        result += "\n"
        curCnt = 0
        continue
    elif i == "<hr>":
        if curCnt != 0:
            result += "\n"

        result += "-" * 80
        result += "\n"
        curCnt = 0
        continue

    if curCnt == 0 and len(i) == 80:
        result += i
        result += '\n'
        curCnt = 0
        continue
    
    if curCnt + len(i) + 1 <= 80:
        if curCnt:
            result += " "
            curCnt += 1
            
        curCnt += len(i)
        result += i
    else: 
        curCnt = len(i)
        result += '\n'
        result += i

    if curCnt == 80:
        result += "\n"
    
print(result)
