l, p = map(int,input().split())
num = list(map(int,input().split()))
for i in range(5):
    n = num[i]
    print(n - l*p, end = " ")
