num = int(input())
size = list(map(int, input().split()))
cl = int(input())
check = 0
for i in range(num):
    if size[i] % cl == 0:
        check += size[i]//cl
    else:
        check += (size[i]//cl+1)
print(cl*check)