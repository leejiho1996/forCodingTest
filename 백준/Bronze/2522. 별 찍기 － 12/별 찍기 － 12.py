n = int(input())

for i in range(n):
    print(' '*(n-1-i), '*'*(i+1), sep="")

for i in range(1, n):
    print(' '*(i), '*'*(n-i),sep="")
