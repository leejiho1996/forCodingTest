#분해합

a = int(input())
g = a

for i in range(1, a+1):
    k = i
    n = list(str(i))
    for j in n:
        k += int(j)
    if k == a and k <= g:
        g = i

if g == a:
    print(0)
    exit()

print(g)