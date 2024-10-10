import sys
input = sys.stdin.readline

a, b = map(int,input().split())

if a > b:
    a, b = b, a

if (b-a) % 2 == 1:
    print((a+b) * ((b-a+1))//2)
else:
    print((a+b) * ((b-a+1)//2) + ((a+b)//2))
