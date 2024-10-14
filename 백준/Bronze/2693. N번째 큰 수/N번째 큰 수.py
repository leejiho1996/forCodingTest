t = int(input())

for i in range(t) :
    n = list(map(int, input().split()))
    n.sort()
    print(n[-3])
