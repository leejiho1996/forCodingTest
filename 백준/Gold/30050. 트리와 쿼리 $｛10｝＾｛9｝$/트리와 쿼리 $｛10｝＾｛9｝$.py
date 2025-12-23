# 트리와 쿼리
import sys
input = sys.stdin.readline

def calDepth(n):

    ret = 0
    
    while n > 0:
        if n in dic:
            n = dic[n]
        else:
            n //= 2

        ret += 1

    return ret

def equalDepth(n, d1, d2):

    ret = 0
    
    while d1 > d2:

        ret += n
        
        if n in dic:
            n = dic[n]
        else:
            n //= 2

        d1 -= 1
        
    return ret, n

Q = int(input())
dic = {}

for i in range(Q):
    c, n1, n2 = map(int,input().split())

    if c == 1:
        dic[n2] = n1
        continue

    result = 0
    
    d1 = calDepth(n1)
    d2 = calDepth(n2)

    if d1 > d2:
        tmp = equalDepth(n1, d1, d2)
        result += tmp[0]
        n1 = tmp[1]
        
    elif d2 > d1:
        tmp = equalDepth(n2, d2 , d1)
        result += tmp[0]
        n2 = tmp[1]
        
    while n1 != n2:

        result += n1
        result += n2
        
        if n1 in dic:
            n1 = dic[n1]
        else:
            n1 //= 2

        if n2 in dic:
            n2 = dic[n2]
        else:
            n2 //= 2

    print(result + n1)
        
