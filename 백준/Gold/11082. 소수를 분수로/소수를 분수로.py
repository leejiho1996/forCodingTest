# 소수를 분수로
import sys
input = sys.stdin.readline

def getGcd(a, b):
    if b > a:
        a, b = b, a

    while b:
        a, b = b, a % b
        
    return a

num = input().rstrip()
if "." not in num:
    print(num,'/',1, sep='')
    exit()
    
natural, decimal = num.split(".")

if "(" not in decimal:
    numer = int(natural+decimal)
    deno = 10**(len(decimal))
    gcd = getGcd(numer, deno)
    print(numer//gcd, "/", deno//gcd, sep="")
else:
    start = decimal.index("(")
    end = decimal.index(")")

    circulation = decimal[start+1:end]
    deno = '9' * len(circulation)
    deno += '0' * decimal.index("(")
    deno = int(deno)
    
    numer = int(natural + decimal[0:start] + circulation)
    numer -= int(natural+decimal[0:start])

    gcd = getGcd(numer, deno)
    
    print(numer//gcd, "/", deno//gcd, sep="")
    