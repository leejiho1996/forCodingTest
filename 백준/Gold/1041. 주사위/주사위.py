# 주사위
import sys
input = sys.stdin.readline

n = int(input())
a, b, c, d, e, f = map(int,input().split())

three = min(a+e+d, a+e+c, a+b+c, a+b+d, f+c+b, f+c+e, f+b+d, f+e+d)
two = min(a+d, a+e, a+c, a+b, b+c, b+d, b+f, c+e, c+f, d+e, d+f, e+f)
one = min(a,b,c,d,e,f)

if n == 1:
    print(a+b+c+d+e+f - max(a,b,c,d,e,f))
elif n == 2:
    print(4 * three + 4 * two)
else:
    cnt3 = 4
    cnt2 = 4 * (n-1) + 4 * (n-2)
    cnt1 = (n-2)**2 * 5 + (n-2) * 4

    print(three * cnt3 + two * cnt2 + one * cnt1)
    
