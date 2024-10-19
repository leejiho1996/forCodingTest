def solution(m, n, startX, startY, balls):
    ans, maxDist = [], m*m + n*n

    for b in balls:
        ans.append(getMinDistance(maxDist, m, n, startX, startY, b[0], b[1]))

    return ans

def getMinDistance(maxDist, m, n, sX, sY, eX, eY):
    res = maxDist

    if sY == eY:
        if sX < eX:
            res = min(res, (sX+eX)**2)
        else:
            res = min(res, (2*m-(sX+eX))**2)

    if sY != eY:
        res = min(res, (sX+eX)**2 + abs(sY-eY)**2)
        res = min(res, (2*m-(sX+eX))**2 + abs(sY-eY)**2)

    if sX == eX:
        if sY < eY:
            res = min(res, (sY+eY)**2)
        else:
            res = min(res, (2*n-(sY+eY))**2)

    if sX != eX:
        res = min(res, (sY+eY)**2 + abs(sX-eX)**2)
        res = min(res, (2*n-(sY+eY))**2 + abs(sX-eX)**2)

    return res