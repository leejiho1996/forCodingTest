#다리 놓기

a = int(input())

for i in range(a):
    b, c = map(int,input().split())
    b_i = 1
    c_i = 1
    for j in range(b):
        b_i *= b
        c_i *= c
        b -= 1
        c -= 1
    print(c_i // b_i)