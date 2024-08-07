first = 31
zero = 30

while True:

    a,b,c = map(int,input().split())

    if a == 0 and b == 0 and c == 0:
        break

    if b == 1 :
        b = 0
    elif b == 2 :
        b = first
    elif b == 3 :
        b = first + 28
    elif b == 4 :
        b = first * 2 + 28
    elif b == 5 :
        b = first * 2 + zero + 28
    elif b == 6 :
        b = first * 3 + zero + 28
    elif b == 7 :
        b = first * 3 + zero * 2 + 28
    elif b == 8 :
        b = first * 4 + zero * 2 + 28
    elif b == 9 :
        b = first * 5 + zero * 2 + 28
    elif b == 10 :
        b = first * 5 + zero * 3 + 28
    elif b == 11 :
        b = first * 6 + zero * 3 + 28
    else :
        b = first * 6 + zero * 4 + 28

    if c % 4 == 0 and c % 100 != 0:
        c = 1
    elif c % 400 == 0 :
        c = 1
    else :
        c = 0

    if b == 0 or b == first :
        c = 0

    print(a + b + c)
