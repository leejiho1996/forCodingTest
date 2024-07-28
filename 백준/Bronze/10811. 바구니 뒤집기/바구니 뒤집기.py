import sys
input = sys.stdin.readline

n, m = map(int,input().split())

basket = [i for i in range(n+1)]

for i in range(m):
    i, j = map(int,input().split())
    copy = basket[i:j+1]

    for n in range(i, j+1):
        basket[n] = copy[j-n]
        
print(*basket[1:])
