# 쿼드트리
import sys
input = sys.stdin.readline

n = int(input())

pic = [input().rstrip() for _ in range(n)]
result = []

def divide(start, end, num):

    word = ''
    total = num**2

    if num == 0:
        return
    
    for i in range(num):
        word += pic[start+i][end:end+num]
                
    if word.count('0') == total:
        result.append('0')
        return
    
    elif word.count('1') == total:
        result.append('1')
        return
    
    else:
        result.append('(')

    num //= 2

    for n_s, n_e in [(0, 0), (0, num), (num, 0), (num, num)]:
        divide(start + n_s, end + n_e, num)

    result.append(')')

divide(0,0, n)
print(*result, sep="")
