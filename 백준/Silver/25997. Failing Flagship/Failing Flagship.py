# Failing Flagship
import sys
input = sys.stdin.readline

def getAngle(direc):
    
    dic = {"N":0, "E":90, "S":180, "W":270, "O":360}

    if direc in dic:
        return dic[direc]
    
    angle = 45

    cur = dic[direc[-1]]

    for i in range(len(direc)-2, -1, -1):

        if cur >= 270:
            key = chr(ord(direc[i]) + 1)
        else:
            key = direc[i]

        nextt = dic.get(key, 0)
        
        if nextt < cur:
            cur -= angle
        else:
            cur += angle

        angle /= 2
        
    return cur

X, Y = input().rstrip().split()

baseX = getAngle(X)
baseY = getAngle(Y)

result = min(baseX, baseY)  + 360 - max(baseX, baseY)
result = min(result, abs(baseX - baseY))

print(result)
