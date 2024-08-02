from functools import reduce
N=input()
length=len(N)


check='NO'
for i in range(1,length):
    one=[int(a) for a in N[:i]]
    two=[int(b) for b in N[i:]]
    
    a=reduce(lambda x, y: x*y, one)
    b=reduce(lambda x, y: x*y, two)
    
    if a==b:
        check="YES"
        break
print(check)